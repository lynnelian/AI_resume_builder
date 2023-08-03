import requests
import json

def llm_request(msg):
    api_key = ""  # 将这里的内容替换成你的 OpenAI API 密钥
    url = "https://proxy.aido.ai/v1/chat/completions" #大神提供的转接gpt服务器
    headers = {"Content-Type": "application/json","Authorization": f"Bearer {api_key}"}
    payload = {'model': "gpt-3.5-turbo","messages": msg,"temperature": 1}
    response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=600)
    #print(response)
    return json.loads(response.text)['choices'][0]['message']['content']

def work_resume_writer(organization,role,keywords):
    prompt = f"你是一个求职辅导教练，擅长为你的学生做职业规则、编写和修改简历等。\
    下面用户会给出学生的企业工作信息的关键词，\
    请你用分点式（1、2、3...）为学生写工作经历描述"

    data = f'''[公司名称]{organization}
    [担任职位]{role}
    [工作内容及业绩]{keywords}
    '''
    msg = [{"role": "system", "content": prompt},{"role": "user", "content": data}]
    return llm_request(msg)

def project_resume_writer(organization,role,keywords):
    prompt = f"你是一个求职辅导教练，擅长为你的学生做职业规则、编写和修改简历等。\
    下面用户会给出学生的项目经验信息的关键词，\
    请你用分点式（1、2、3...）为学生写项目经历描述"

    data = f'''[项目名称]{organization}
    [担任角色]{role}
    [工作内容及业绩]{keywords}
    '''
    msg = [{"role": "system", "content": prompt},{"role": "user", "content": data}]
    return llm_request(msg)

def self_intro_writer(input_keywords,input_wordcount,experience=""):
    prompt = f"你是一个求职辅导教练，擅长为你的学生做职业规则、编写和修改简历等。\
    下面学生会给出他的关键词和过往经历，请你为学生编写一段{input_wordcount}字左右的个人简介放在简历上。"
    experience = experience if experience else "无"
    data = f'''[关键词]{input_keywords}
    [过往经历]{experience}
    '''
    msg = [{"role": "system", "content": prompt},{"role": "user", "content": data}]
    return llm_request(msg)