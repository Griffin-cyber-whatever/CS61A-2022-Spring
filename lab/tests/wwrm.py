test = {
  'name': 'wwrm',
  'points': 0,
  'suites': [
    {
        'type': 'concept',
        'cases': [
        {
          'question': r"""#[a-f0-9]{6}""",
          'choices': ['Any 6-digit hexadecimal color code, like #fdb515', 'A hexadecimal color code that starts with letters and ends with numbers, like #gg1234', 'Any hexadecimal color code with 0-6 digits', 'A hexadecimal color code with 3 letters and 3 numbers'],
          'answer': 'Any 6-digit hexadecimal color code, like #fdb515',
        },
        {
          'question': r"""
          (fizz(buzz|)|buzz)
          """,
          'choices': ['Only fizzbuzz', 'Only fizz', 'Only fizzbuzz, fizz, and buzz', 'Only fizzbuzzbuzz', 'Only fizzbuzz or buzz'],
          'answer': 'Only fizzbuzz, fizz, and buzz',
        },
        {
          'question': r"""
          [-+]?\d*\.?\d+
          """,
          'choices': ['Signed or unsigned numbers like +1000, -1.5, .051', 'Only unsigned numbers like 0.051', 'Only signed numbers like +1000, -1.5',
          'Only signed or unsigned integers like +1000, -33'],
          'answer': 'Signed or unsigned numbers like +1000, -1.5, .051',
        },
        {
          'question': r"""
          [1-9]+[05]+
          """,
          'choices': ['Numbers that are both greater than 5 and divisible by 5 like 10, 25, 800', 
          'Numbers that are divisible by 5 like 5, 20, 6325', 'Any positive number', 
          'Numbers that are divisible by 5 but do not have the digits 0 and 5 adjacent to each other as the last 2 digits'],
          'answer': 'Numbers that are both greater than 5 and divisible by 5 like 10, 25, 800',
        }
      ]
    }
  ]
}