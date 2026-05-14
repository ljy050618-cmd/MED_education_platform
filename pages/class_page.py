from urllib.parse import quote
from fastapi import Request
from nicegui import ui


def register_class_page():


    @ui.page('/class')
    def class_page(request: Request):
        name = request.query_params.get('name', '학생')
        student_id = request.query_params.get('student_id', '000000')

        with ui.column().classes('w-full min-h-screen bg-slate-50'):

            # 상단 헤더
            with ui.element('div').classes(
                'w-full min-h-[64px] sm:min-h-[76px] flex flex-col sm:flex-row '
                'items-start sm:items-center justify-between gap-3 px-4 sm:px-8 lg:px-10 '
                'py-4 sm:py-0 bg-white border-b border-slate-200'
            ):
                with ui.column().classes('gap-0'):
                    ui.label('AMPhST Research Lab').classes(
                        'text-xl sm:text-2xl font-bold text-slate-800'
                    )
                    ui.label('아주대학교 의사과학자 양성사업단').classes(
                        'text-xs sm:text-sm text-slate-400'
                    )

                with ui.row().classes('items-center gap-2 sm:gap-5 flex-wrap'):
                    ui.label(f'{name} · {student_id}').classes(
                        'text-sm sm:text-base font-medium text-slate-600'
                    )

                    ui.button('한국어', icon='language').props('flat dense').classes(
                        'text-slate-500 text-sm'
                    )

                    ui.button(
                        '로그아웃',
                        icon='logout',
                        on_click=lambda: ui.navigate.to('/')
                    ).props('flat dense').classes(
                        'text-slate-500 text-sm'
                    )

            # 본문
            with ui.column().classes(
                'w-full px-4 sm:px-8 lg:px-12 py-6 sm:py-10 gap-6 sm:gap-8'
            ):

                # 환영 영역
                with ui.card().classes(
                    'w-full p-6 sm:p-10 rounded-3xl shadow-sm bg-white border border-slate-100'
                ):
                    ui.label('WELCOME RESEARCHER').classes(
                        'text-xs sm:text-sm font-semibold tracking-widest text-blue-500'
                    )

                    with ui.row().classes('items-baseline gap-2 sm:gap-3 mt-3 flex-wrap'):
                        ui.label(f'{name}').classes(
                            'text-3xl sm:text-4xl font-semibold text-slate-900 leading-none'
                        )
                        ui.label('연구자님, 환영합니다.').classes(
                            'text-2xl sm:text-3xl font-semibold text-slate-700 leading-none'
                        )

                    ui.label(
                        '임상 문제를 연구 질문으로 바꾸고, 연구 설계를 단계별로 완성해보세요.'
                    ).classes(
                        'text-base sm:text-lg text-slate-500 mt-5'
                    )

                    with ui.row().classes('gap-2 sm:gap-3 mt-6 flex-wrap'):
                        ui.label('Research Design').classes(
                            'px-3 sm:px-4 py-2 rounded-full bg-slate-100 text-slate-600 text-xs sm:text-sm font-medium'
                        )
                        ui.label('Clinical Data').classes(
                            'px-3 sm:px-4 py-2 rounded-full bg-slate-100 text-slate-600 text-xs sm:text-sm font-medium'
                        )
                        ui.label('Ethics').classes(
                            'px-3 sm:px-4 py-2 rounded-full bg-slate-100 text-slate-600 text-xs sm:text-sm font-medium'
                        )

                # 미션 카드 영역
                with ui.element('div').classes(
                    'w-full grid grid-cols-1 md:grid-cols-3 gap-6'
                ):

                    with ui.card().classes(
                        'w-full min-h-[220px] sm:min-h-[260px] p-6 sm:p-7 rounded-3xl shadow-sm bg-white border border-slate-100'
                    ):
                        ui.label('Mission 01').classes(
                            'text-sm font-semibold text-blue-500'
                        )
                        ui.label('연구설계 실습').classes(
                            'text-xl sm:text-2xl font-bold text-slate-900 mt-3'
                        )
                        ui.label(
                            '연구 질문, 대상자, 변수, 분석 방법을 선택하며 연구 설계를 완성합니다.'
                        ).classes(
                            'text-sm sm:text-base text-slate-500 mt-3 leading-relaxed'
                        )
                        ui.space()
                        ui.button(
                            '시작하기',
                            icon='arrow_forward',
                            on_click=lambda: ui.navigate.to(
                                f'/genre?name={quote(name)}&student_id={quote(student_id)}'
                            )
                        ).classes(
                            'mt-6 w-full py-3 rounded-xl bg-blue-600 text-white'
                        )

                    with ui.card().classes(
                        'w-full min-h-[220px] sm:min-h-[260px] p-6 sm:p-7 rounded-3xl shadow-sm bg-white border border-slate-100'
                    ):
                        ui.label('Mission 02').classes(
                            'text-sm font-semibold text-emerald-500'
                        )
                        ui.label('데이터 해석 훈련').classes(
                            'text-xl sm:text-2xl font-bold text-slate-900 mt-3'
                        )
                        ui.label(
                            '가상의 임상 데이터를 보고 변수의 의미와 연구 결과를 해석합니다.'
                        ).classes(
                            'text-sm sm:text-base text-slate-500 mt-3 leading-relaxed'
                        )
                        ui.space()
                        ui.button('준비 중').props('outline').classes(
                            'mt-6 w-full py-3 rounded-xl text-slate-500'
                        )

                    with ui.card().classes(
                        'w-full min-h-[220px] sm:min-h-[260px] p-6 sm:p-7 rounded-3xl shadow-sm bg-white border border-slate-100'
                    ):
                        ui.label('Mission 03').classes(
                            'text-sm font-semibold text-purple-500'
                        )
                        ui.label('연구윤리 체크').classes(
                            'text-xl sm:text-2xl font-bold text-slate-900 mt-3'
                        )
                        ui.label(
                            'IRB, 개인정보, 비식별화, 연구대상자 보호 원칙을 점검합니다.'
                        ).classes(
                            'text-sm sm:text-base text-slate-500 mt-3 leading-relaxed'
                        )
                        ui.space()
                        ui.button('준비 중').props('outline').classes(
                            'mt-6 w-full py-3 rounded-xl text-slate-500'
                        )

                    with ui.card().classes(
                        'w-full min-h-[220px] sm:min-h-[260px] p-6 sm:p-7 rounded-3xl shadow-sm bg-white border border-slate-100'
                    ):
                        ui.label('Mission 04').classes(
                            'text-sm font-semibold text-rose-500'
                        )

                        ui.label('문제풀이 훈련').classes(
                            'text-xl sm:text-2xl font-bold text-slate-900 mt-3'
                        )

                        ui.label(
                            '연구 개념과 논문 내용을 바탕으로 핵심 문제를 풀며 이해도를 점검합니다.'
                        ).classes(
                            'text-sm sm:text-base text-slate-500 mt-3 leading-relaxed'
                        )

                        ui.space()

                        ui.button(
                            '시작하기',
                            icon='arrow_forward',
                            on_click=lambda: ui.navigate.to(
                                f'/quiz?name={quote(name)}&student_id={quote(student_id)}'
                            )
                        ).classes(
                            'mt-6 w-full py-3 rounded-xl bg-rose-600 text-white'
                        )
            

                # 하단 안내
                with ui.card().classes(
                    'w-full p-5 sm:p-6 rounded-2xl bg-slate-100 shadow-none'
                ):
                    ui.label(
                        '학습 기록은 실제 인증 없이 체험용으로만 표시됩니다.'
                    ).classes(
                        'text-sm text-slate-500'
                    )
