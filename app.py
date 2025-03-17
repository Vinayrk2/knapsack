from flask import Flask, render_template, request

app = Flask(__name__)

# Knapsack Algorithm Implementation
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    explanation = []

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
                explanation.append(
                    f"Item {i-1}: Weight={weights[i-1]}, Value={values[i-1]} | "
                    f"Max({dp[i-1][w]}, {values[i-1]} + {dp[i-1][w-weights[i-1]]}) = {dp[i][w]}"
                )
            else:
                dp[i][w] = dp[i - 1][w]
                explanation.append(
                    f"Item {i-1}: Weight={weights[i-1]} exceeds remaining capacity {w}, skipping."
                )

    # Tracking selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()

    # Calculate weight usage percentage for visualization bar
    weight_used = sum(weights[i] for i in selected_items)
    weight_used_percentage = round((weight_used / capacity) * 100, 2)

    return {
        "maxValue": dp[n][capacity],
        "selectedItems": selected_items,
        "explanation": explanation,
        "weightUsedPercentage": weight_used_percentage,
        "weights": weights
    }

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            values = list(map(int, request.form['values'].split(',')))
            weights = list(map(int, request.form['weights'].split(',')))
            capacity = int(request.form['capacity'])

            if len(values) != len(weights):
                raise ValueError("Values and weights must have the same number of elements.")

            result = knapsack(values, weights, capacity)
        except ValueError as e:
            result = {"error": str(e)}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)