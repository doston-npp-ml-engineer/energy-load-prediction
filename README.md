# Energy Load Prediction (Decision Tree)

This project predicts energy load types (Light, Medium, Maximum) using a Decision Tree model.

## Dataset
Steel Industry Energy Consumption (2018)

## Steps
- Feature engineering (hour, month, day)
- Encoding categorical variables
- Model training with Decision Tree
- Hyperparameter tuning using GridSearchCV

## Result
- Accuracy: ~94–95%
- Balanced performance across all classes

## Note
The model was initially overfitting to the NSM feature, so it was removed and retrained.
