import json

# The raw JSON response from the API error
raw_response = '{"code":2,"message":"API parameter invalid","errors":[{"error":"invalid_value","invalidValue":null,"location":"gasPrice","message":"\'gasPrice\' field may not be empty when \'FeeLevel PriorityFee MaxFee\' fields are not set (was null)"},{"error":"invalid_value","invalidValue":null,"location":"gasLimit","message":"\'gasLimit\' field may not be empty when \'FeeLevel\' field is not set (was null)"},{"constraints":{"min":"1"},"error":"min_value","invalidValue":null,"location":"amounts","message":"\'amounts\' field must be greater than 1 (was [])"}]}'

# Parse and prettify
try:
    parsed = json.loads(raw_response)
    print('🔴 API Error Response (Prettified):')
    print('=' * 50)
    print(json.dumps(parsed, indent=2))
    
    print('\n📋 Error Summary:')
    print('=' * 50)
    print(f'Code: {parsed["code"]}')
    print(f'Message: {parsed["message"]}')
    print(f'Total Errors: {len(parsed["errors"])}')
    
    print('\n🚨 Individual Errors:')
    print('=' * 50)
    for i, error in enumerate(parsed['errors'], 1):
        print(f'{i}. Location: {error["location"]}')
        print(f'   Error Type: {error["error"]}')
        print(f'   Message: {error["message"]}')
        if 'constraints' in error:
            print(f'   Constraints: {error["constraints"]}')
        print()
        
except json.JSONDecodeError as e:
    print(f'Error parsing JSON: {e}')
