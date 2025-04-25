exercise_1_1_hint = """이 연습 문제의 채점 함수는 정확한 아라비아 숫자 "1", "2", "3"을 포함하는 답변을 찾고 있습니다.
종종 Claude에게 원하는 것을 단순히 요청하는 것만으로도 원하는 결과를 얻을 수 있습니다."""

exercise_1_2_hint = """이 연습 문제의 채점 함수는 "soo" 또는 "giggles"를 포함하는 답변을 찾고 있습니다.
이것을 해결하는 방법은 여러 가지가 있으며, 단순히 요청하는 것만으로도 가능합니다!"""

exercise_2_1_hint ="""이 연습 문제의 채점 함수는 "hola"라는 단어를 포함하는 모든 답변을 찾고 있습니다.
인간과 대화할 때처럼 Claude에게 스페인어로 답변해달라고 요청하세요. 정말 간단합니다!"""

exercise_2_2_hint = """이 연습 문제의 채점 함수는 정확히 "Michael Jordan"을 찾고 있습니다.
다른 사람에게 이것을 어떻게 요청하겠습니까? 다른 단어 없이 답변하라고요? 이름만 답변하고 다른 것은 없게 하라고요? 이 문제에 접근하는 방법은 여러 가지가 있습니다."""

exercise_2_3_hint = """이 셀의 채점 함수는 800단어 이상의 응답을 찾고 있습니다.
LLM은 아직 단어 수를 세는 것이 완벽하지 않기 때문에, 목표보다 더 많은 단어를 요청해야 할 수도 있습니다."""

exercise_3_1_hint = """이 연습 문제의 채점 함수는 "incorrect" 또는 "not correct"라는 단어를 포함하는 답변을 찾고 있습니다.
Claude에게 수학 문제를 더 잘 해결할 수 있는 역할을 부여해보세요!"""

exercise_4_1_hint = """이 연습 문제의 채점 함수는 "haiku"와 "pig"라는 단어를 포함하는 해결책을 찾고 있습니다.
주제를 대체하고 싶은 곳에 정확한 구문 "{TOPIC}"을 포함하는 것을 잊지 마세요. "TOPIC" 변수 값을 변경하면 Claude가 다른 주제에 대한 하이쿠를 작성하게 됩니다."""

exercise_4_2_hint = """이 연습 문제의 채점 함수는 "brown"이라는 단어를 포함하는 응답을 찾고 있습니다.
"{QUESTION}"을 XML 태그로 감싸면 Claude의 응답이 어떻게 변하나요?"""

exercise_4_3_hint = """이 연습 문제의 채점 함수는 "brown"이라는 단어를 포함하는 응답을 찾고 있습니다.
가장 의미가 적은 부분부터 시작하여 한 번에 한 단어 또는 문자 섹션을 제거해 보세요. 한 번에 한 단어씩 이렇게 하면 Claude가 얼마나 많이 또는 적게 구문을 분석하고 이해할 수 있는지 확인하는 데도 도움이 됩니다."""

exercise_5_1_hint = """이 연습 문제의 채점 함수는 "Warrior"라는 단어를 포함하는 응답을 찾고 있습니다.
Claude의 목소리로 더 많은 단어를 작성하여 Claude가 원하는 방식으로 행동하도록 유도하세요. 예를 들어, "Stephen Curry는 최고입니다. 왜냐하면"이라고 쓰는 대신 "Stephen Curry는 최고이며 다음은 그 이유 세 가지입니다. 1:"이라고 쓸 수 있습니다."""

exercise_5_2_hint = """채점 함수는 "cat"과 "<haiku>"라는 단어를 포함하는 5줄 이상의 길이의 응답을 찾고 있습니다.
간단하게 시작하세요. 현재 프롬프트는 Claude에게 하나의 하이쿠를 요청합니다. 이를 변경하여 두 개(또는 더 많은) 하이쿠를 요청할 수 있습니다. 그런 다음 형식 문제가 발생하면, Claude가 이미 하나 이상의 하이쿠를 작성한 후에 프롬프트를 변경하여 그 문제를 해결하세요."""

exercise_5_3_hint = """이 연습 문제의 채점 함수는 "tail", "cat", "<haiku>"라는 단어를 포함하는 응답을 찾고 있습니다.
이 연습 문제를 여러 단계로 나누는 것이 도움이 됩니다.								
1.	Claude가 두 개의 시를 쓰도록 초기 프롬프트 템플릿을 수정하세요.							
2.	Claude에게 시가 무엇에 관한 것인지 표시를 주되, 주제를 직접 작성하는 대신(예: 개, 고양이 등) 해당 주제를 "{ANIMAL1}"과 "{ANIMAL2}" 키워드로 대체하세요.							
3.	프롬프트를 실행하고 변수 대체가 있는 전체 프롬프트에 모든 단어가 올바르게 대체되었는지 확인하세요. 그렇지 않은 경우, {괄호} 태그의 철자와 형식이 올바른지, 단일 중괄호로 올바르게 형식이 지정되었는지 확인하세요."""

exercise_6_1_hint = """이 연습 문제의 채점 함수는 "C) B" 또는 "B) B" 등과 같이 올바른 분류 문자 + 닫는 괄호와 카테고리 이름의 첫 글자를 찾고 있습니다.
이 연습 문제를 단계별로 살펴보겠습니다:										
1.	Claude는 어떤 카테고리를 사용하고 싶은지 어떻게 알 수 있을까요? 알려주세요! 원하는 네 가지 카테고리를 프롬프트에 직접 포함시키세요. 쉬운 분류를 위해 괄호 안의 문자도 포함시키세요. XML 태그를 사용하여 프롬프트를 구성하고 Claude에게 카테고리가 어디서 시작하고 끝나는지 명확하게 알려주세요.									
2.	Claude가 즉시 분류만으로 답변하도록 불필요한 텍스트를 줄이세요. 이를 위한 여러 방법이 있습니다. Claude를 위해 말하기(답변의 첫 부분으로 괄호 안의 문자를 원한다는 것을 Claude가 알 수 있도록 문장의 시작부터 단일 열린 괄호까지 제공)부터 Claude에게 분류만 원한다고 말하고 서문을 건너뛰는 것까지 다양합니다.
이러한 기술에 대한 복습이 필요하면 2장과 5장을 참조하세요.							
3.	Claude가 여전히 잘못 분류하거나 답변에 카테고리 이름을 포함하지 않을 수 있습니다. Claude에게 답변에 전체 카테고리 이름을 포함하도록 지시하여 이 문제를 해결하세요.								
4.	Claude가 평가할 이메일을 적절히 대체할 수 있도록 프롬프트 템플릿에 {email}이 여전히 있는지 확인하세요."""

exercise_6_1_solution = """
USER TURN
다음 카테고리로 이 이메일을 분류해주세요: {email}

카테고리 외에 다른 단어는 포함하지 마세요.

<categories>
(A) 판매 전 질문
(B) 고장 또는 결함 있는 제품
(C) 결제 질문
(D) 기타 (설명해주세요)
</categories>

ASSISTANT TURN
(
"""

exercise_6_2_hint = """이 연습 문제의 채점 함수는 "<answer>B</answer>"와 같이 <answer> 태그로 감싸진 올바른 문자만 찾고 있습니다. 올바른 분류 문자는 위 연습 문제와 동일합니다.
때로는 Claude가 원하는 출력 형식의 예를 제공하는 것이 가장 간단한 방법입니다. 예시를 <example></example> 태그로 감싸는 것을 잊지 마세요! 그리고 Claude의 응답을 미리 채우면 Claude가 실제로 그 부분을 응답의 일부로 출력하지 않는다는 것을 잊지 마세요."""

exercise_7_1_hint = """Claude를 위해 몇 가지 예제 이메일을 작성하고 분류해야 합니다(원하는 정확한 형식으로). 이를 수행하는 방법은 여러 가지가 있습니다. 아래에 몇 가지 지침이 있습니다.										
1.	최소한 두 개의 예제 이메일을 갖도록 노력하세요. Claude는 모든 카테고리에 대한 예제가 필요하지 않으며, 예제가 길 필요도 없습니다. 더 까다롭다고 생각하는 카테고리에 대한 예제를 제공하는 것이 더 도움이 됩니다(6장 연습 문제 1의 하단에서 생각해보라고 요청받았던 것). XML 태그는 예제를 프롬프트의 나머지 부분과 분리하는 데 도움이 되지만, 필수는 아닙니다.									
2.	예제 답변 형식이 Claude가 사용하기를 원하는 형식과 정확히 일치하도록 하여 Claude가 형식을 모방할 수 있도록 하세요. 이 형식은 Claude의 답변이 카테고리의 문자로 끝나도록 해야 합니다. {email} 자리 표시자를 어디에 두든, 예제 이메일과 정확히 같은 형식으로 지정되었는지 확인하세요.									
3.	프롬프트 자체 내에 카테고리가 여전히 나열되어 있는지 확인하세요. 그렇지 않으면 Claude가 참조할 카테고리를 알 수 없습니다. 또한 대체를 위한 자리 표시자로 {email}도 포함해야 합니다."""

exercise_7_1_solution = """
USER TURN
다음 카테고리로 이메일을 분류하고, 설명을 포함하지 마세요: 
<categories>
(A) 판매 전 질문
(B) 고장 또는 결함 있는 제품
(C) 결제 질문
(D) 기타 (설명해주세요)
</categories>

다음은 올바른 답변 형식의 몇 가지 예입니다:
<examples>
Q: Mixmaster4000을 구매하는 데 얼마가 드나요?
A: 올바른 카테고리는: A

Q: 제 Mixmaster가 켜지지 않습니다.
A: 올바른 카테고리는: B

Q: 메일링 리스트에서 저를 제거해 주세요.
A: 올바른 카테고리는: D
</examples>

분류할 이메일은 다음과 같습니다: {email}

ASSISTANT TURN
올바른 카테고리는:
"""
exercise_8_1_hint = """이 연습 문제의 채점 함수는 "I do not", "I don't" 또는 "Unfortunately"라는 구문을 포함하는 응답을 찾고 있습니다.
Claude가 답을 모를 경우 어떻게 해야 할까요?"""

exercise_8_2_hint = """이 연습 문제의 채점 함수는 "49-fold"라는 구문을 포함하는 응답을 찾고 있습니다.
Claude가 먼저 관련 인용구를 추출하고 인용구가 충분한 증거를 제공하는지 여부를 확인하여 작업과 사고 과정을 보여주도록 하세요. 복습이 필요하면 8장 수업을 참조하세요."""

exercise_9_1_solution = """
당신은 세무 전문가입니다. 제공된 참조 문서를 사용하여 사용자 질문에 답변하는 것이 당신의 임무입니다.

사용자의 질문에 답변하기 위해 사용해야 할 자료는 다음과 같습니다:
<docs>
{TAX_CODE}
</docs>

다음은 응답 방법의 예입니다:
<example>
<question>
"자격을 갖춘" 직원을 정의하는 것은 무엇인가요?
</question>
<answer>
<quotes>이 하위 섹션의 목적상—
(A)일반적으로
"자격을 갖춘 직원"이라는 용어는 다음과 같은 개인을 의미합니다—
(i)제외된 직원이 아니며,
(ii)이 하위 섹션에 따라 이루어진 선택에서 자격을 갖춘 주식과 관련하여 24장에 따른 법인의 원천징수 요건이 충족되도록 하기 위해 장관이 필요하다고 결정한 요건을 충족하는 데 동의합니다.</quotes>

<answer>제공된 문서에 따르면, "자격을 갖춘 직원"은 다음과 같은 개인으로 정의됩니다:

1. 문서에 정의된 "제외된 직원"이 아닌 사람.
2. 자격을 갖춘 주식과 관련하여 24장에 따른 법인의 원천징수 요건을 충족하기 위해 장관이 결정한 요건을 충족하는 데 동의한 사람.</answer>
</example>

먼저 사용자의 질문에 답변하는 데 관련된 인용구를 <quotes></quotes> 태그 안에 수집하세요. 인용구가 없는 경우 "관련 인용구를 찾을 수 없음"이라고 작성하세요.

그런 다음 사용자 질문에 답변하기 전에 두 개의 단락 구분을 삽입하고 <answer></answer> 태그 안에 답변하세요. <quotes></quotes> 태그 안의 인용구가 답변을 뒷받침한다고 확신하는 경우에만 사용자의 질문에 답변하세요. 그렇지 않은 경우, 사용자에게 질문에 답변할 수 있는 충분한 정보가 없다고 알려주세요.

다음은 사용자 질문입니다: {QUESTION}
"""

exercise_9_2_solution = """
당신은 Codebot으로, 코드의 문제를 찾고 가능한 개선 사항을 제안하는 도움이 되는 AI 어시스턴트입니다.

사용자가 배울 수 있도록 돕는 소크라테스식 튜터 역할을 하세요.

사용자로부터 일부 코드가 제공될 것입니다. 다음을 수행하세요:
1. 코드의 문제를 식별하세요. 각 문제를 별도의 <issues> 태그 안에 넣으세요.
2. 사용자에게 문제를 해결하기 위해 코드의 수정된 버전을 작성하도록 초대하세요.

다음은 예시입니다:

<example>
<code>
def calculate_circle_area(radius):
    return (3.14 * radius) ** 2
</code>
<issues>
<issue>
3.14가 제곱되고 있지만 실제로는 반지름만 제곱되어야 합니다>
</issue>
<response>
거의 맞았지만, 연산 순서와 관련된 문제가 있습니다. 원의 공식을 작성한 다음 코드의 괄호를 자세히 살펴보는 것이 도움이 될 수 있습니다.
</response>
</example>

분석할 코드는 다음과 같습니다:

<code>
{CODE}
</code>

관련 문제를 찾고 소크라테스식 튜터 스타일의 응답을 작성하세요. 사용자에게 너무 많은 도움을 주지 마세요! 대신, 사용자가 스스로 올바른 해결책을 찾을 수 있도록 안내만 제공하세요.

각 문제를 <issue> 태그에 넣고 최종 응답을 <response> 태그에 넣으세요.
"""

exercise_10_2_1_solution = """system_prompt = system_prompt_tools_general_explanation + \"""다음은 JSONSchema 형식으로 사용 가능한 함수입니다:

<tools>

<tool_description>
<tool_name>get_user</tool_name>
<description>
사용자 ID로 데이터베이스에서 사용자를 검색합니다.
</description>
<parameters>
<parameter>
<name>user_id</name>
<type>int</type>
<description>검색할 사용자의 ID입니다.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>get_product</tool_name>
<description>
제품 ID로 데이터베이스에서 제품을 검색합니다.
</description>
<parameters>
<parameter>
<name>product_id</name>
<type>int</type>
<description>검색할 제품의 ID입니다.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_user</tool_name>
<description>
데이터베이스에 새 사용자를 추가합니다.
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>사용자의 이름입니다.</description>
</parameter>
<parameter>
<name>email</name>
<type>str</type>
<description>사용자의 이메일 주소입니다.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_product</tool_name>
<description>
데이터베이스에 새 제품을 추가합니다.
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>제품의 이름입니다.</description>
</parameter>
<parameter>
<name>price</name>
<type>float</type>
<description>제품의 가격입니다.</description>
</parameter>
</parameters>
</tool_description>

</tools>
"""
