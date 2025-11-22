import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';
import 'dart:io';
import 'package:http/http.dart' as http;

class DocumentUploadScreen extends StatefulWidget {
  const DocumentUploadScreen({super.key});

  @override
  State<DocumentUploadScreen> createState() => _DocumentUploadScreenState();
}

class _DocumentUploadScreenState extends State<DocumentUploadScreen> {
  File? _selectedFile;
  String _uploadStatus = '';

  Future<void> _pickFile() async {
    FilePickerResult? result = await FilePicker.platform.pickFiles(
      type: FileType.custom,
      allowedExtensions: ['pdf', 'doc', 'docx', 'png', 'jpg', 'jpeg'],
    );

    if (result != null) {
      setState(() {
        _selectedFile = File(result.files.single.path!);
        _uploadStatus = 'File selected: ${result.files.single.name}';
      });
    }
  }

  Future<void> _uploadFile() async {
    if (_selectedFile == null) return;

    setState(() {
      _uploadStatus = 'Uploading...';
    });

    var request = http.MultipartRequest(
      'POST',
      Uri.parse('http://10.0.2.2:8000/upload'), // Android Emulator localhost
    );
    request.files.add(
      await http.MultipartFile.fromPath('file', _selectedFile!.path),
    );

    try {
      var response = await request.send();
      if (response.statusCode == 200) {
        setState(() {
          _uploadStatus = 'Upload successful! Processing...';
        });
        // TODO: Handle response (summary, etc.)
      } else {
        setState(() {
          _uploadStatus = 'Upload failed: ${response.statusCode}';
        });
      }
    } catch (e) {
      setState(() {
        _uploadStatus = 'Error: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Upload Policy')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            if (_selectedFile != null)
              Text('Selected: ${_selectedFile!.path.split('/').last}'),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _pickFile,
              child: const Text('Pick File (PDF/Image/Word)'),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _selectedFile != null ? _uploadFile : null,
              child: const Text('Upload & Analyze'),
            ),
            const SizedBox(height: 20),
            Text(_uploadStatus),
          ],
        ),
      ),
    );
  }
}
