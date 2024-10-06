def countdown(n: int) -> list:  # No need to worry about this code right now
    """
    This function takes an integer `n` and returns a list counting down from n to 1.

    Parameters:
    n (int): The starting number for the countdown.

    Returns:
    list: A list containing numbers from n down to 1.

    Note: You don't need to worry about the 'def' line or 'return' statement right now.
    Just focus on writing the correct expressions in the provided lines and fixing errors.
    """

    # Create an empty list to store the countdown numbers
    result = []

    # Use a failsafe counter to prevent the loop from running too long
    iteration_count = 0

    # Start a while loop to count down from n to 1
    while (
        n > 0 and iteration_count < 100
    ):  # Stops after 100 iterations to avoid infinite loop
        result.append(n)  # This line adds the current number (n) to the list
        n = n + 1
        iteration_count += (
            1  # This line updates the failsafe counter, no need to modify it!
        )

    # The return statement sends the result list back
    return result  # No need to worry about this code right now
