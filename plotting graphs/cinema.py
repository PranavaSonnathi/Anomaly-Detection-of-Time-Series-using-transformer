import csv
import matplotlib.pyplot as plt

# Load the data from CSV
X = []
with open('C:\\Users\\saisr\\OneDrive\\Desktop\\Project School\\cinemaTicket_Ref.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        X.append(float(row['tickets_sold']))  # Convert to float

# Function to calculate moments
def calculate_moments(data):
    n = len(data)
    mean_data = sum(data) / n
    var_data = sum((x - mean_data) ** 2 for x in data) / n
    skew_data = sum((x - mean_data) ** 3 for x in data) / (n * (var_data ** 1.5))
    kurt_data = sum((x - mean_data) ** 4 for x in data) / (n * (var_data ** 2)) - 3
    return mean_data, var_data, skew_data, kurt_data

# Now, proceed with analysis
n = len(X)
mean_X, var_X, skew_X, kurt_X = calculate_moments(X)

# Plot X(t)
t = range(n)
plt.scatter(t, X)
plt.title("Scatter Plot of X(t)")
plt.xlabel("Time (t)")
plt.ylabel("X(t) - Movie Ticket Sales")
plt.show()

# 3. Estimate A(t) = (X - E(X)) and plot
A = [(x - mean_X) for x in X]
mean_A, var_A, skew_A, kurt_A = calculate_moments(A)
plt.scatter(t, A,color='green')
plt.title("Scatter Plot of A(t) = X(t) - E(X)")
plt.xlabel("Time (t)")
plt.ylabel("A(t)")
plt.show()

# 4. Estimate B(t) = (A - E(A)) and plot
B = [(a - mean_A) for a in A]
mean_B, var_B, skew_B, kurt_B = calculate_moments(B)
plt.scatter(t, B,color='purple')
plt.title("Scatter Plot of B(t) = A(t) - E(A)")
plt.xlabel("Time (t)")
plt.ylabel("B(t)")
plt.show()

# 5. Estimate C(t) = (B - E(B)) and plot
C = [(b - mean_B) for b in B]
mean_C, var_C, skew_C, kurt_C = calculate_moments(C)
plt.scatter(t, C,color='red')
plt.title("Scatter Plot of C(t) = B(t) - E(B)")
plt.xlabel("Time (t)")
plt.ylabel("C(t)")
plt.show()

# 6. Observations: You can look at the graphs and interpret patterns.
print(f"Moments of A(t): Mean: {mean_A}, Variance: {var_A}, Skewness: {skew_A}, Kurtosis: {kurt_A}")
print(f"Moments of B(t): Mean: {mean_B}, Variance: {var_B}, Skewness: {skew_B}, Kurtosis: {kurt_B}")
print(f"Moments of C(t): Mean: {mean_C}, Variance: {var_C}, Skewness: {skew_C}, Kurtosis: {kurt_C}")

# 7. Identify outliers using a simple threshold
# Outliers could be defined as points more than 3 standard deviations away from the mean
threshold = 3
outliers = [x for x in X if abs(x - mean_X) > threshold * (var_X ** 0.5)]

print(f"Identified {len(outliers)} outliers.")