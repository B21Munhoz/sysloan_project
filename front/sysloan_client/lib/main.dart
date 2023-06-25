import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

const url = "http://0.0.0.0:8000/";
Future<FormConfig> fetchFormFields() async {
  final response = await http
      .get(Uri.parse('${url}get_form_fields/'));
  try {
    if (response.statusCode == 200) {
      // If the server did return a 200 OK response,
      // then parse the JSON.
      return FormConfig.fromJson(jsonDecode(response.body));
    } else {
      // If the server did not return a 200 OK response,
      // then throw an exception.
      throw Exception('Failed to load form');
    }
  } catch (e) {
    throw Exception(e.toString());
  }
}

void main() => runApp(const MyApp());

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class FormConfig {
  final List<String> formFields;

  const FormConfig({
    required this.formFields,
  });

  factory FormConfig.fromJson(Map<String, dynamic> json) {
    return FormConfig(
      formFields: json['fields'].cast<String>()
    );
  }
}
class _MyAppState extends State<MyApp> {
  late Future<FormConfig> futureFieldList;

  @override
  void initState() {
    super.initState();
    futureFieldList = fetchFormFields();
  }

  @override
  Widget build(BuildContext context) {
    final formKey = GlobalKey<FormState>();
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Desafio DigitalSys',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Desafio DigitalSys'),
        ),
        body: Center(
          child: FutureBuilder<FormConfig>(
            future: futureFieldList,
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                var fieldsList = snapshot.data!.formFields;
                var formWidgets = <Widget>[];
                var formMap = {
                  "cpf": "",
                  "proposal_info": {}
                };
                var proposalInfo = {};
                formWidgets.add(
                      Container(
                        constraints: const BoxConstraints(maxWidth: 400),
                        child: Row(
                          children: [
                            const Text(
                              "cpf", 
                              style: TextStyle(
                                fontWeight: FontWeight.bold,
                                fontSize: 18
                                )),
                            const Spacer(),
                            SizedBox(
                              width: 300,
                              child: TextFormField(
                                onChanged: (val){
                                  formMap["cpf"] = val;
                                },
                                validator: (val) {
                                  if (val == null){
                                    return "Forneça um CPF válido!";
                                  } else if (val.length != 11) {
                                    return "Forneça um CPF válido!";
                                  } else if (!RegExp(r'^[0-9]+$').hasMatch(val)){
                                    return "Forneça apenas os números sem pontos ou traços!";
                                  }
                                  return null;
                                },
                              ),
                            ),
                          ],
                        ),
                      )
                    );
                for(var i = 0; i < fieldsList.length; i++){
                    proposalInfo[fieldsList[i]] = '';
                    formWidgets.add(
                      Container(
                        constraints: const BoxConstraints(maxWidth: 400),
                        child:Row(
                          children: [
                            Text(
                              fieldsList[i], 
                              style: const TextStyle(
                                fontWeight: FontWeight.bold,
                                fontSize: 18
                                )),
                            const Spacer(),
                            SizedBox(
                              width: 300,
                              child: TextFormField(
                                onChanged: (val){
                                  proposalInfo[fieldsList[i]] = val;
                                },
                              ),
                            ),
                          ],
                        ),
                      )
                    );
                }

                return ListView(
                  shrinkWrap: true,
                  children: <Widget>[
                    Container(
                      padding: const EdgeInsets.only(top: 10.00, left: 10.00),
                      child: Text(
                        "Formulário de Empréstimo",
                        textAlign: TextAlign.center,
                        style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 30,
                              color: Colors.blue.shade900
                              )
                      ),
                    ),
                    const SizedBox(height: 100),
                    Form(
                      key: formKey,
                      child: Column(children: formWidgets,),
                    ),
                    const SizedBox(height: 50),
                    ClipRRect(
                      borderRadius: BorderRadius.circular(30.0),
                      child: Container(
                        alignment: Alignment.center,
                        constraints: const BoxConstraints(
                          maxWidth: 100,
                          maxHeight: 70,
                        ),
                        child: TextButton(
                          style: TextButton.styleFrom(
                            foregroundColor: Colors.white,
                            padding: const EdgeInsets.all(16.0),
                            textStyle: const TextStyle(fontSize: 20),
                            backgroundColor: Colors.blue.shade900
                          ),
                          onPressed: () async {
                            formMap["proposal_info"] = proposalInfo;
                            final form = formKey.currentState as FormState;
                              if (form.validate()) {
                                var response = await http.post(
                                  Uri.parse('${url}send_proposal/'),
                                  headers: {"Content-Type": "application/json"},
                                  body: json.encode(formMap)
                                );
                                if (response.statusCode == 201){
                                  formKey.currentState?.reset();
                                  ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
                                    content: Text("Proposta Enviada!"),
                                  ));
                                } else {
                                  formKey.currentState?.reset();
                                  ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                                    content: Text("Algo deu Errado. Tente de novo. ${response.statusCode}"),
                                  ));
                                }
                              }
                          },
                          child: const Text('Enviar'),
                        ),
                      )
                    )
                  ],
                );
              } else if (snapshot.hasError) {
                return Text('${snapshot.error}');
              }

              // By default, show a loading spinner.
              return const CircularProgressIndicator();
            },
          ),
        ),
      ),
    );
  }
}