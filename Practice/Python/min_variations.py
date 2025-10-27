def minimizeVariation(productSize):
    productSize.sort()
    total = 0
    min_so_far = productSize[0]
    max_so_far = productSize[0]

    for i in range(len(productSize)):
        min_so_far = min(min_so_far, productSize[i])
        max_so_far = max(max_so_far, productSize[i])
        total += max_so_far - min_so_far

    return total

if __name__ == "__main__":
    # Ask user how many products
    n = int(input("Enter number of products: "))

    # Ask for product sizes
    productSize = list(map(int, input("Enter product sizes (space-separated): ").split()))

    # Validate length
    if len(productSize) != n:
        print("❌ Error: Number of sizes entered does not match n")
    else:
        result = minimizeVariation(productSize)
        print("✅ Minimum total variation after rearranging:", result)