```python
import sys
from src.chatbot import generate_response
from src.analytics import analyze_performance
from src.payment_system import process_payment
from src.user_interface import UserInterface
from src.integration import integrate_social_media
from src.compatibility import check_compatibility

def main():
    # Check compatibility
    if not check_compatibility(sys.platform):
        print("This platform is not supported.")
        return

    # Initialize user interface
    ui = UserInterface()

    # Main loop
    while True:
        # Display main menu
        ui.display_main_menu()

        # Get user input
        choice = ui.get_user_choice()

        # Process user choice
        if choice == '1':
            # Generate chatbot response
            message = ui.get_user_message()
            response = generate_response(message)
            ui.display_chatbot_response(response)
        elif choice == '2':
            # Analyze performance
            report = analyze_performance()
            ui.display_performance_report(report)
        elif choice == '3':
            # Process payment
            payment_info = ui.get_payment_info()
            result = process_payment(payment_info)
            ui.display_payment_result(result)
        elif choice == '4':
            # Integrate with social media
            integrate_social_media()
        elif choice == '5':
            # Exit
            break
        else:
            ui.display_error_message("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```