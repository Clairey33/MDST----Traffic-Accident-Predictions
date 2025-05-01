import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

class AccidentSeverityModel(nn.Module):
    def __init__(self):
        super(AccidentSeverityModel, self).__init__()
        self.fc1 = nn.Linear(9, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 4)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.3)
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.xavier_uniform_(self.fc2.weight)

    def forward(self, x):
        # TODO: Implement the forward pass using fc1, dropout
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = AccidentSeverityModel()
model.load_state_dict(torch.load('accident_severity_model.pth'))
model.eval()

# Use default features for every prediction
features = {
    'Traffic_Signal_Flag': 0,
    'Crossing_Flag': 0,
    'Highway_Flag': 1,
    # 'Distance(mi)': -0.3,
    'Distance(mi)': 25 ,
    'Start_Hour_Sin': 0.0,
    'Start_Hour_Cos': 1.0, 
    'Start_Month_Sin': 0.0,
    'Start_Month_Cos': 1.0,
    'Accident_Duration': -0.02
}

def predict_severity():
    # TODO: Create a tensor from the feature values, pass it through the model, and return the predicted severity (add 1 to the output class index)
    feature_values = np.array(list(features.values()), dtype=np.float32)
    feature_tensor = torch.tensor(feature_values).unsqueeze(0)
    with torch.no_grad():
        output = model(feature_tensor)
    _, predicted = torch.max(output, 1)

    return predicted.item() + 1  




proj = ccrs.PlateCarree()
fig, ax = plt.subplots(subplot_kw=dict(projection=proj), figsize=(11, 6))
ax.set_extent([-125, -65, 24, 50], crs=ccrs.PlateCarree())

# TODO: Copy and paste what you did for week8_map_m.py 
# Add map features (land, ocean, lakes, borders, states, coastline)
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
ax.add_feature(cfeature.LAKES, facecolor='lightblue', alpha=0.5)
ax.add_feature(cfeature.BORDERS, linestyle='-')
ax.add_feature(cfeature.STATES, linestyle='-')
ax.coastlines(resolution='10m', color='black')

ax.set_title("Click on a location to predict severity", fontsize=14, pad=20)

red_dot = None

def on_click(event):
    # TODO: When user clicks on the map, show a red dot and update the title with predicted severity at that location
    global red_dot 
    if event.inaxes == ax:
        if red_dot:
            red_dot.remove()
        red_dot = ax.plot(event.xdata, event.ydata, 'ro', markersize=6, transform=ccrs.Geodetic())[0]
        severity = predict_severity()
        ax.set_title(f"Clicked: ({event.xdata:.2f}, {event.ydata:.2f}) | Predicted Severity: {severity}", fontsize=14, pad=20)
        fig.canvas.draw()

fig.canvas.mpl_connect('button_press_event', on_click)

plt.subplots_adjust(top=0.88)
plt.show()
