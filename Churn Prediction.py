

# Calculate total duration and total amount spent per customer
customer_stats = df.groupby('Customer ID').agg(
    total_duration=('Duration (hours)', 'sum'),
    total_amount_spent=('Amount Spent (INR)', 'sum'),
    num_visits=('Customer ID', 'count'),
    first_visit=('Date', 'min'),
    last_visit=('Date', 'max')
).reset_index()

# Calculate additional features
customer_stats['average_session_duration'] = customer_stats['total_duration'] / customer_stats['num_visits']
customer_stats['frequency_of_visits'] = (customer_stats['last_visit'] - customer_stats['first_visit']).dt.days / customer_stats['num_visits']


customer_stats.head()
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Define churn: a customer who hasn't visited in the last 3 months
reference_date = pd.to_datetime('2024-06-01')
customer_stats['is_churn'] = (reference_date - customer_stats['last_visit']).dt.days > 90

# Prepare data for modeling
features = ['total_duration', 'total_amount_spent', 'num_visits', 'average_session_duration', 'frequency_of_visits']
X = customer_stats[features]
y = customer_stats['is_churn']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Feature importances
feature_importances = pd.Series(clf.feature_importances_, index=features).sort_values(ascending=False)
print(feature_importances)
