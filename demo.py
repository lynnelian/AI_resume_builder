import gradio as gr
from main import work_resume_writer,project_resume_writer,self_intro_writer

with gr.Blocks() as demo:
    gr.Markdown(
        """<center><h1>AI简历编写助手</h1></center>
        </br>
        <h3>说明：AI简历编写助手是一款基于大模型技术的智能应用，旨在帮助您快速、高效地编写个人简历内容。
        </br>
        您只要填写关键词，该应用将自动生成工作经历、项目经历、自我介绍等内容，极大地简化了简历撰写的过程，提高了您求职的效率和准确性。
        </br>
        请您在以下每项栏目填入信息（关键词至少要三个，越多越好哦）：</h3>
        """
        )
    with gr.Tab("工作经历"):
        with gr.Column():
            organization_w = gr.Textbox(lines=1,label="公司名称：")
            role_w = gr.Textbox(lines=1,label="担任职位：")
            keywords_w = gr.Textbox(lines=1,label="工作内容及业绩：")
            button_work = gr.Button("生成工作描述")
            output_work = gr.Textbox(lines=2, label="生成结果：")
    with gr.Tab("项目经历"):
        with gr.Column():
            organization_p = gr.Textbox(lines=1,label="项目名称：")
            role_p = gr.Textbox(lines=1,label="担任角色：")
            keywords_p = gr.Textbox(lines=1,label="工作内容及业绩：")
            button_project = gr.Button("生成项目描述")
            output_project = gr.Textbox(lines=2, label="生成结果：")
    with gr.Tab("自我介绍"):
        with gr.Column():
            input_keywords = gr.Textbox(lines=2,label="你的关键词：")
            input_wordcount = gr.Textbox(lines=2,label="需求字数：")
            button_self_intro = gr.Button("一键生成")
            output_self_intro = gr.Textbox(lines=2, label="生成结果：")

    button_work.click(work_resume_writer, inputs=[organization_w, role_w, keywords_w], outputs=output_work)
    button_project.click(project_resume_writer, inputs=[organization_p,role_p,keywords_p], outputs=output_project)
    button_self_intro.click(self_intro_writer, inputs=[input_keywords,input_wordcount], outputs=output_self_intro)

demo.launch()