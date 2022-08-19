import json
d ={
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "content",
      "resource": {
        "resourceType": "Bundle",
        "meta": {
          "lastUpdated": "2022-01-18T21:53:01.000+01:00",
          "profile": [
            "https://demis.rki.de/fhir/StructureDefinition/NotificationBundleLaboratory"
          ]
        },
        "identifier": {
          "system": "https://demis.rki.de/fhir/NamingSystem/NotificationBundleId",
          "value": "cfac9539-65ec-371e-9eb8-0bd59faa2c13"
        },
        "type": "document",
        "timestamp": "2022-01-18T21:53:01.000+01:00",
        "entry": [
          {
            "fullUrl": "https://demis.rki.de/fhir/Composition/0a40505c-e003-3f50-a659-6dc47fb6d702",
            "resource": {
              "resourceType": "Composition",
              "id": "0a40505c-e003-3f50-a659-6dc47fb6d702",
              "meta": {
                "profile": [
                  "https://demis.rki.de/fhir/StructureDefinition/NotificationLaboratory"
                ]
              },
              "identifier": {
                "system": "https://demis.rki.de/fhir/NamingSystem/NotificationId",
                "value": "f6628903-73f6-4edb-a008-62b363739769"
              },
              "status": "final",
              "type": {
                "coding": [
                  {
                    "system": "http://loinc.org",
                    "code": "34782-3",
                    "display": "Infectious disease Note"
                  }
                ]
              },
              "category": [
                {
                  "coding": [
                    {
                      "system": "http://loinc.org",
                      "code": "11502-2",
                      "display": "Laboratory report"
                    }
                  ]
                }
              ],
              "subject": {
                "reference": "Patient/1993e4b9-a985-37fa-bdd9-1a198f4f740c"
              },
              "date": "2022-01-18T21:53:00.000+01:00",
              "author": [
                {
                  "reference": "PractitionerRole/2324ba55-f6d4-3294-a2e0-7e48532c912f"
                }
              ],
              "title": "Erregernachweismeldung",
              "section": [
                {
                  "code": {
                    "coding": [
                      {
                        "system": "http://loinc.org",
                        "code": "11502-2",
                        "display": "Laboratory report"
                      }
                    ]
                  },
                  "entry": [
                    {
                      "reference": "DiagnosticReport/f961bfed-ce9d-319b-9371-ab0cb68a3694"
                    }
                  ]
                }
              ]
            }
          },
          {
            "fullUrl": "https://demis.rki.de/fhir/Patient/1993e4b9-a985-37fa-bdd9-1a198f4f740c",
            "resource": {
              "resourceType": "Patient",
              "id": "1993e4b9-a985-37fa-bdd9-1a198f4f740c",
              "meta": {
                "profile": [
                  "https://demis.rki.de/fhir/StructureDefinition/NotifiedPerson"
                ]
              },
              "name": [
                {
                  "use": "official",
                  "family": "Tester",
                  "given": [
                    "Testus"
                  ]
                }
              ],
              "gender": "male",
              "birthDate": "1978-12-12",
              "address": [
                {
                  "extension": [
                    {
                      "url": "https://demis.rki.de/fhir/StructureDefinition/AddressUse",
                      "valueCoding": {
                        "system": "https://demis.rki.de/fhir/CodeSystem/addressUse",
                        "code": "primary"
                      }
                    }
                  ],
                  "line": [
                    "Teststr. 123"
                  ],
                  "city": "Lauenburg",
                  "postalCode": "21481",
                  "country": "20422"
                }
              ]
            }
          },
          {
            "fullUrl": "https://demis.rki.de/fhir/PractitionerRole/2324ba55-f6d4-3294-a2e0-7e48532c912f",
            "resource": {
              "resourceType": "PractitionerRole",
              "id": "2324ba55-f6d4-3294-a2e0-7e48532c912f",
              "meta": {
                "profile": [
                  "https://demis.rki.de/fhir/StructureDefinition/NotifierRole"
                ]
              },
              "organization": {
                "reference": "Organization/7e88b9a1-9dcd-3a8c-b8ac-635b40c58d3a"
              }
            }
          },
          {
            "fullUrl": "https://demis.rki.de/fhir/Organization/7e88b9a1-9dcd-3a8c-b8ac-635b40c58d3a",
            "resource": {
              "resourceType": "Organization",
              "id": "7e88b9a1-9dcd-3a8c-b8ac-635b40c58d3a",
              "meta": {
                "profile": [
                  "https://demis.rki.de/fhir/StructureDefinition/NotifierFacility"
                ]
              },
              "identifier": [
                {
                  "system": "https://demis.rki.de/fhir/NamingSystem/DemisLaboratoryId",
                  "value": "12345"
                },
                {
                  "system": "https://fhir.kbv.de/NamingSystem/KBV_NS_Base_BSNR",
                  "value": "98765430"
                }
              ],
              "type": [
                {
                  "coding": [
                    {
                      "system": "https://demis.rki.de/fhir/CodeSystem/organizationType",
                      "code": "laboratory",
                      "display": "Erregerdiagnostische Untersuchungsstelle"
                    }
                  ]
                }
              ],
              "name": "Primärlabor",
              "telecom": [
                {
                  "system": "phone",
                  "value": "0309876543210",
                  "use": "work"
                }
              ],
              "address": [
                {
                  "line": [
                    "Dingsweg 321"
                  ],
                  "city": "Berlin",
                  "postalCode": "13055",
                  "country": "20422"
                }
              ]
            }
          },
          {
            "fullUrl": "https://demis.rki.de/fhir/PractitionerRole/7b7a0980-bd67-30ba-a154-e80198aa636a",
            "resource": {
              "resourceType": "PractitionerRole",
              "id": "7b7a0980-bd67-30ba-a154-e80198aa636a",
              "meta": {
                "profile": [
                  "https://demis.rki.de/fhir/StructureDefinition/SubmittingRole"
                ]
              },
              "organization": {
                "reference": "Organization/e23656d0-d040-36ea-b96c-2df37914aaeb"
              }
            }
          },
          {
            "fullUrl": "https://demis.rki.de/fhir/Organization/e23656d0-d040-36ea-b96c-2df37914aaeb",
            "resource": {
              "resourceType": "Organization",
              "id": "e23656d0-d040-36ea-b96c-2df37914aaeb",
              "meta": {
                "profile": [
                  "https://demis.rki.de/fhir/StructureDefinition/SubmittingFacility"
                ]
              },
              "identifier": [
                {
                  "system": "https://fhir.kbv.de/NamingSystem/KBV_NS_Base_BSNR",
                  "value": "123456780"
                }
              ],
              "name": "Einsendepraxis ABC",
              "telecom": [
                {
                  "system": "phone",
                  "value": "030 1234567890",
                  "use": "work"
                }
              ],
              "address": [
                {
                  "line": [
                    "Teststr. 123"
                  ],
                  "city": "Berlin",
                  "postalCode": "13055",
                  "country": "20422"
                }
              ]
            }
          },
          {
            "fullUrl": "https://demis.rki.de/fhir/DiagnosticReport/f961bfed-ce9d-319b-9371-ab0cb68a3694",
            "resource": {
              "resourceType": "DiagnosticReport",
              "id": "f961bfed-ce9d-319b-9371-ab0cb68a3694",
              "meta": {
                "profile": [
                  "https://demis.rki.de/fhir/StructureDefinition/LaboratoryReportMYTP"
                ]
              },
              "basedOn": [
                {
                  "type": "ServiceRequest",
                  "identifier": {
                    "system": "https://demis.rki.de/fhir/NamingSystem/ServiceRequestId",
                    "value": "2022-000000001"
                  }
                }
              ],
              "status": "final",
              "code": {
                "coding": [
                  {
                    "system": "https://demis.rki.de/fhir/CodeSystem/notificationCategory",
                    "code": "mytp",
                    "display": "Mycobacterium tuberculosis, Mycobacterium africanum, Mycobacterium bovis; Meldepflicht für den direkten Erregernachweis sowie nachfolgend für das Ergebnis der Resistenzbestimmung; vorab auch für den Nachweis säurefester Stäbchen im Sputum"
                  }
                ]
              },
              "subject": {
                "reference": "Patient/1993e4b9-a985-37fa-bdd9-1a198f4f740c"
              },
              "issued": "2022-01-18T21:52:00.000+01:00",
              "result": [
                {
                  "reference": "Observation/cd4c07cf-dbd7-3178-b3b1-8f431f792fa5"
                }
              ],
              "conclusion": "Ich bin die textuelle Conclusion ...",
              "conclusionCode": [
                {
                  "coding": [
                    {
                      "system": "https://demis.rki.de/fhir/CodeSystem/conclusionCode",
                      "code": "pathogenDetected",
                      "display": "Meldepflichtiger Erreger nachgewiesen"
                    }
                  ]
                }
              ]
            }
          },
          {
            "fullUrl": "https://demis.rki.de/fhir/Observation/cd4c07cf-dbd7-3178-b3b1-8f431f792fa5",
            "resource": {
              "resourceType": "Observation",
              "id": "cd4c07cf-dbd7-3178-b3b1-8f431f792fa5",
              "meta": {
                "profile": [
                  "https://demis.rki.de/fhir/StructureDefinition/PathogenDetectionMYTP"
                ]
              },
              "status": "final",
              "category": [
                {
                  "coding": [
                    {
                      "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                      "code": "laboratory"
                    }
                  ]
                }
              ],
              "code": {
                "coding": [
                  {
                    "system": "http://loinc.org",
                    "code": "72357-7",
                    "display": "Microscopic observation [Presence] in Specimen by Acid fast stain"
                  }
                ]
              },
              "subject": {
                "reference": "Patient/1993e4b9-a985-37fa-bdd9-1a198f4f740c"
              },
              "valueCodeableConcept": {
                "coding": [
                  {
                    "system": "http://loinc.org",
                    "code": "LA11882-0",
                    "display": "Detected"
                  }
                ]
              },
              "interpretation": [
                {
                  "coding": [
                    {
                      "system": "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation",
                      "code": "POS",
                      "display": "Positive"
                    }
                  ]
                }
              ],
              "note": [
                {
                  "text": "Nette Zusatzinformation"
                }
              ],
              "specimen": {
                "reference": "Specimen/394b3d61-4be7-3989-b053-7bd473617e77"
              }
            }
          },
          {
            "fullUrl": "https://demis.rki.de/fhir/Specimen/394b3d61-4be7-3989-b053-7bd473617e77",
            "resource": {
              "resourceType": "Specimen",
              "id": "394b3d61-4be7-3989-b053-7bd473617e77",
              "meta": {
                "profile": [
                  "https://demis.rki.de/fhir/StructureDefinition/SpecimenMYTP"
                ]
              },
              "status": "available",
              "type": {
                "coding": [
                  {
                    "system": "http://snomed.info/sct",
                    "code": "119334006",
                    "display": "Sputum specimen (specimen)"
                  }
                ]
              },
              "subject": {
                "reference": "Patient/1993e4b9-a985-37fa-bdd9-1a198f4f740c"
              },
              "receivedTime": "2022-01-18T16:27:00.000+01:00",
              "collection": {
                "collector": {
                  "reference": "PractitionerRole/7b7a0980-bd67-30ba-a154-e80198aa636a"
                },
                "collectedDateTime": "2022-01-18T11:27:00.000+01:00"
              },
              "note": [
                {
                  "text": "Ich bin eine interessante Zusatzinformation ..."
                }
              ]
            }
          }
        ]
      }
    }
  ]
}

#print(d)
dj = json.dumps(d)

#how to access resources
#d['parameter'][0]['resource']['entry'][7]['resource']
