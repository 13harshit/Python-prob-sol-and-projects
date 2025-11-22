# How to Setup Firebase for Policy Simplifier App

## 1. Create a Firebase Project
1.  Go to the [Firebase Console](https://console.firebase.google.com/).
2.  Click **"Add project"** (or "Create a project").
3.  Enter a name (e.g., `PolicySimplifier`).
4.  Disable Google Analytics (optional, easier for setup) and click **"Create project"**.
5.  Once created, click **"Continue"** to enter the project dashboard.

## 2. Enable Authentication
1.  In the left sidebar, click **Build** -> **Authentication**.
2.  Click **"Get started"**.
3.  Select **"Email/Password"** from the Sign-in method list.
4.  Enable the **"Email/Password"** toggle and click **"Save"**.

## 3. Link to Flutter App (Using FlutterFire CLI)
*Note: You need `Node.js` installed for this.*

1.  **Install Firebase CLI** (if not done):
    Open your terminal and run:
    ```bash
    npm install -g firebase-tools
    ```
2.  **Login to Firebase**:
    ```bash
    firebase login
    ```
3.  **Install FlutterFire CLI**:
    ```bash
    dart pub global activate flutterfire_cli
    ```
4.  **Configure the App**:
    Navigate to your project folder (`PolicySimplifierApp/frontend`) and run:
    ```bash
    dart pub global run flutterfire_cli:flutterfire configure
    ```
    *(If `flutterfire` command works for you, you can use that too, but the above command is safer if PATH is not set)*

    -   Select your project (`policysimplifier-...`).
    -   Select platforms (Android, iOS).
    -   This will generate `lib/firebase_options.dart`.

## 4. Finalize Code
1.  Open `lib/main.dart`.
2.  Uncomment the Firebase initialization lines (I have already added the imports).

```dart
// In lib/main.dart
await Firebase.initializeApp(
  options: DefaultFirebaseOptions.currentPlatform,
);
```
