import json

RESULT_TEMPLATE = '''
<div id="questions" class="accordion">
{}
</div>
'''

WRAPPER_TEMPLATE = '''
<div class="accordion-item question">
    <h2 class="accordion-header" id="panelsStayOpen-heading-{0}">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse-{0}" aria-expanded="true" aria-controls="panelsStayOpen-collapse-{0}">
       {0}. {1}
      </button>
    </h2>
    <div id="panelsStayOpen-collapse-{0}" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading-{0}">
      <div class="accordion-body">
        {2}
      </div>
    </div>
  </div>
'''

ANS_WRAPPER_TEMPLATE = '''
<ul class="list-group">
    {}
</ul>
'''

ANS_TEMPLATE = '''
    <li class="list-group-item">{}</li>
'''


result = ''
with open('QUESTIONS.json', 'r') as f:
    data = f.read()

questions = json.loads(data)
l = len(questions)
for i in range(l):
    q = questions[i]
    formatted_ans_lst = []
    for ans in q['answers']:
        formatted_ans_lst.append(ANS_TEMPLATE.format(ans))
    formatted_ans = ANS_WRAPPER_TEMPLATE.format(
        ''.join(formatted_ans_lst))

    result += WRAPPER_TEMPLATE.format(i+1, q['question'], formatted_ans)

result = RESULT_TEMPLATE.format(result)

print(result)
