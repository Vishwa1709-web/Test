import gradio as gr


def image(image):
    return image

def select_all(choice):
    if choice:
        return[True, True, True, True,True, True,True, True,True, True,True, True,True, True,True ]
    else:
        return[False, False, False, False,False, False,False, False,False, False,False, False,False, False,False]

with gr.Blocks() as demo:
    # img = gr.Image()
    with gr.Row():
            with gr.Column(scale=1, min_width=800):
                    with gr.Row():
                        text1 = gr.Textbox(label="Product ID")
                        drop1 = gr.Dropdown([], label="Category")
                    with gr.Row():
                        text2 = gr.Textbox(label="Specific text to be mentioned", scale=2)
                        model_btn = gr.Button("Extract Metadata")
                    with gr.Row():
                        c1 = gr.Checkbox(min_width=1, container=False, label='Select All')
                    with gr.Row():
                                text3 = gr.Textbox(label="Sub Category")
                                c2 = gr.Checkbox(min_width=1, container=False, label='')
                                text4 = gr.Textbox(label="Brand Name")
                                c3 = gr.Checkbox(min_width=1, container=False, label='')
                                text5 = gr.Textbox(label="Product Name")
                                c4 = gr.Checkbox(min_width=1, container=False, label='')
                                text6 = gr.Textbox(label="Gender")
                                c5 = gr.Checkbox(min_width=1, container=False, label='')
                    with gr.Row():
                                text7 = gr.Textbox(label="Material")
                                c6 = gr.Checkbox(min_width=1, container=False, label='')
                                text8 = gr.Textbox(label="Colour")
                                c7 = gr.Checkbox(min_width=1, container=False, label='')
                                text9 = gr.Textbox(label="Pattern")
                                c8 = gr.Checkbox(min_width=1, container=False, label='')
                                text10 = gr.Textbox(label="Style")
                                c9 = gr.Checkbox(min_width=1, container=False, label='')
                    with gr.Row():
                                text11 = gr.Textbox(label="Sleeve Length")
                                c10 = gr.Checkbox(min_width=1, container=False, label='')
                                text12 = gr.Textbox(label="Neckline")
                                c11 = gr.Checkbox(min_width=1, container=False, label='')
                                text13 = gr.Textbox(label="Occasion")
                                c12 = gr.Checkbox(min_width=1, container=False, label='')
                                text14 = gr.Textbox(label="Season")
                                c13 = gr.Checkbox(min_width=1, container=False, label='')
                    with gr.Row():
                                text15 = gr.Textbox(label="Mood", scale=2)
                                c14 = gr.Checkbox(min_width=0, container=False, label='')
                                text16 = gr.Textbox(label="Surrounding", scale=2)
                                c15 = gr.Checkbox(min_width=0, container=False, label='')
                                export_btn = gr.Button("Export as CSV", scale=4)
                    c1.select(fn=select_all, inputs=c1, outputs=[c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15])
                    with gr.Row():
                            text17 = gr.Textbox(label="Suggested Search Keywords")
                    with gr.Row():
                            text18 = gr.Textbox(label="Product Description(detailed)")        
                    with gr.Row():
                            text19 = gr.Textbox(label="Product Description(short)")                
                    with gr.Row():
                            drop2 = gr.Dropdown([], label="Campaign Goals")
                            text20 = gr.Textbox(label="Target Audience Demographics")
                            gr.CheckboxGroup(['Video Ad', 'Image Ad'], label="Ad Formats", container=True)
                    with gr.Row():
                            text21 = gr.Textbox(label="Ad copy(4 options)")
                            text22 = gr.Textbox(" ")
                            text23 = gr.Textbox(" ")
                            text24 = gr.Textbox(" ")
                    with gr.Row():
                            text25 = gr.Textbox(label="CTA Text")
                            text26 = gr.Textbox(" ")        
                            inbtw = gr.Button("Regenerate")
            with gr.Column(scale=2, min_width=600):
                with gr.Row():
                        img1 = gr.Image(label="Input Image", height=500)
                        img2 = gr.Image(label="Enhanced Catalouge Image", height=500)

                img3 = gr.Image(label="Image Ad")
                img4 = gr.Video(label="Video Ad")
                
            
if __name__ == "__main__":
    demo.launch()