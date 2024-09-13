import flet as ft
from flet_core.types import CrossAxisAlignment
from flet_core.border_radius import horizontal


def main(page: ft.Page):
    page.title= "¿me perdonas?"
    page.bgcolor= "pink"
    page.horizontal_alignment=CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    lbl1=ft.Text("¿me perdonas?",
            style=ft.TextStyle(size=20,weight="bold"))
    img1=ft.Image(src="triste.png",width=200,height=200)
    
    btnSi=ft.ElevatedButton("si",
                            color="green",
                            width=100,
                            height=50
                            )
    btnNo=ft.ElevatedButton("no",
                            color="red",
                            width=100,
                            height=50
                            )
    
    def no(e):
        btnSi.width+=30
        btnNo.height+=10
        page.update()
        
        def si(e):
            img1.scr="feliz.png"
            page.update()
            
            btnNo.on_click=no
            btnSi.on_click=si
            
            page.add(
                ft.column(
                    [
                        lbl1,
                        img1,
                        ft.Row(
                            [btnSi,btnNo],
                            alignment=ft.MainAxisAlignment.CENTER
                        
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignmt=ft.CrossAxisAlignment,
                    spacing=20
                    
                    
                )
            )

ft.app(main)
