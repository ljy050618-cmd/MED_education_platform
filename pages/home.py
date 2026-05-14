from urllib.parse import quote
from nicegui import ui


def register_home_page():

    @ui.page('/')
    def index():

        with ui.column().classes(
            'w-full min-h-screen items-center justify-center bg-white'
        ) as page:
            pass

        def show_logo_page():
            page.clear()

            with page:
                with ui.column().classes('w-full min-h-screen items-center justify-center px-4'):
                    with ui.row().classes(
                        'items-center justify-center gap-3 sm:gap-4 flex-wrap text-center'
                    ):
                        ui.image('/education_images/Ajou_logo.png').classes(
                            'w-[52px] h-[52px] sm:w-[68px] sm:h-[68px]'
                        )

                        with ui.row().classes('items-center gap-3 sm:gap-4 flex-wrap justify-center'):

                            # 왼쪽 글자
                            with ui.column().classes('gap-0 items-end'):
                                ui.label('아주대학교').classes(
                                    'text-2xl sm:text-4xl font-bold text-gray-900 leading-tight'
                                )
                                ui.label('AJOU UNIVERSITY').classes(
                                    'text-sm sm:text-xl font-semibold text-gray-700 leading-tight'
                                )

                            # 가운데 세로선
                            ui.element('div').classes(
                                'w-[2px] h-[52px] sm:h-[72px] bg-gray-400'
                            )

                            # 오른쪽 글자
                            with ui.column().classes('gap-0 items-start'):
                                ui.label('의과대학').classes(
                                    'text-2xl sm:text-4xl font-bold text-gray-900 leading-tight'
                                )
                                ui.label('School of Medicine').classes(
                                    'text-sm sm:text-xl font-semibold text-gray-700 leading-tight'
                                )

        def show_program_page():
            page.clear()

            with page:
                with ui.column().classes(
                    'w-full min-h-screen items-center justify-center bg-white px-4 text-center'
                ):
                    ui.label('아주대학교 의사과학자 양성사업단').classes(
                        'text-xl sm:text-3xl font-semibold text-gray-400'
                    )

                    ui.label('AMPhST 프로그램').classes(
                        'text-3xl sm:text-5xl font-bold text-gray-400 mt-3 sm:mt-4'
                    )

                    ui.label('의사과학자 연구설계 랩을 준비하고 있습니다').classes(
                        'text-base sm:text-lg text-gray-400 mt-8 sm:mt-10'
                    )

                    ui.spinner(size='lg').classes('mt-2')

        def show_main_page():
            page.clear()

            with page:
                with ui.column().classes(
                    'relative w-full min-h-screen items-center justify-center bg-white px-4 text-center'
                ):

                    # 좌측 상단 사업단 문구
                    with ui.column().classes(
                        'absolute top-4 left-4 sm:top-8 sm:left-8 items-start gap-1 text-left'
                    ):
                        ui.label('아주대학교 의사과학자 양성사업단').classes(
                            'text-xs sm:text-base font-medium text-gray-400'
                        )
                        ui.label('AMPhST 프로그램').classes(
                            'text-sm sm:text-xl font-semibold text-gray-400'
                        )

                    ui.label('의사과학자 연구설계 랩').classes(
                        'text-3xl sm:text-4xl font-bold text-gray-900 text-center'
                    )

                    ui.label('학생이 연구자 입장에서 연구 설계를 체험하는 학습용 사이트입니다.').classes(
                        'text-base sm:text-lg text-gray-600 mt-3 px-4'
                    )

                    ui.button(
                        '연구 미션 시작하기',
                        on_click=show_login_page
                    ).classes(
                        'text-base sm:text-lg px-5 sm:px-6 py-3 mt-6'
                    )

        def show_login_page():
            page.clear()

            with page:
                with ui.column().classes(
                    'relative w-full min-h-screen items-center justify-center bg-white px-4 py-20'
                ):

                    # 좌측 상단 사업단 문구
                    with ui.column().classes(
                        'absolute top-4 left-4 sm:top-8 sm:left-8 items-start gap-1 text-left'
                    ):
                        ui.label('아주대학교 의사과학자 양성사업단').classes(
                            'text-xs sm:text-base font-medium text-gray-400'
                        )
                        ui.label('AMPhST 프로그램').classes(
                            'text-sm sm:text-xl font-semibold text-gray-400'
                        )

                    # 로그인 카드
                    with ui.card().classes(
                        'w-full max-w-[420px] p-6 sm:p-8 rounded-2xl shadow-lg items-center'
                    ):
                        ui.label('연구자 로그인').classes(
                            'text-2xl sm:text-3xl font-bold text-gray-900 text-center'
                        )

                        ui.label('학습 체험을 위해 정보를 입력하세요.').classes(
                            'text-sm sm:text-base text-gray-500 text-center mt-2'
                        )

                        name_input = ui.input('이름').props('dense').classes(
                            'w-full mt-5 sm:mt-6'
                        )

                        ui.input('이메일').props('dense').classes(
                            'w-full'
                        )

                        student_id_input = ui.input('학번 또는 참가번호').props('dense').classes(
                            'w-full'
                        )

                        def go_class_page():
                            name = quote(name_input.value or '학생')
                            student_id = quote(student_id_input.value or '000000')
                            ui.navigate.to(f'/class?name={name}&student_id={student_id}')

                        ui.button(
                            '로그인',
                            on_click=go_class_page
                        ).classes(
                            'w-full text-base sm:text-lg py-3 mt-4'
                        )

                        ui.label('※ 실제 인증 없이 학습 체험용으로 사용됩니다.').classes(
                            'text-xs text-gray-400 mt-3 text-center'
                        )

        show_logo_page()

        ui.timer(5.0, show_program_page, once=True)
        ui.timer(8.0, show_main_page, once=True)
