# Policy Simplifier App - Setup Instructions

## Backend Setup (Python)
1.  Navigate to `backend` directory:
    ```bash
    cd PolicySimplifierApp/backend
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Important**: For OCR to work, you must install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) on your system and ensure it's in your PATH.
4.  Run the server:
    ```bash
    uvicorn main:app --reload
    ```
    The server will start at `http://127.0.0.1:8000`.

## Frontend Setup (Flutter)
1.  Navigate to `frontend` directory:
    ```bash
    cd PolicySimplifierApp/frontend
    ```
2.  Install dependencies:
    ```bash
    flutter pub get
    ```
3.  **Firebase Setup**:
    -   Create a project in Firebase Console.
    -   Run `flutterfire configure` to generate `firebase_options.dart`.
    -   Uncomment the Firebase initialization code in `lib/main.dart`.
4.  Run the app:
    ```bash
    flutter run
    ```
    *Note: For Android Emulator, the backend URL is `http://10.0.2.2:8000`.*

## Features Implemented
-   **Authentication**: Login/Signup UI (Firebase integration ready).
-   **Document Upload**: File picker for PDFs/Images.
-   **Backend Analysis**: Endpoint for OCR, Summarization, and Simplification (Mocked/Ready for Models).
-   **Chatbot**: Chat UI and Backend Endpoint.
