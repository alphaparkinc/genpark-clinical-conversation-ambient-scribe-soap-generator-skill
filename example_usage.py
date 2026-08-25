from client import ClinicalConversationAmbientScribeSoapGeneratorClient

def main():
    client = ClinicalConversationAmbientScribeSoapGeneratorClient()
    res = client.generate_clinical_soap_note('ENC_INTERNAL_MED_5501')
    print('Encounter: ' + res['encounter_id'] + ' (Time Saved: ' + str(res['physician_documentation_time_saved_pct']) + '%)')
    print('Subjective: ' + res['subjective_summary'])
    print('ICD-10 Codes: ' + ', '.join(res['assessment_icd10_codes']))
    print('FHIR Synced: ' + str(res['ehr_epic_cerner_fhir_json_synced']))

if __name__ == '__main__':
    main()
