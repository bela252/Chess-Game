# ============================================================
# CHESS GAME - COMMENTED VERSION
# هذا هو نفس ملف المشروع، مع إضافة تعليقات عربية توضيحية.
# التعليقات لا تغيّر طريقة عمل البرنامج.
# المكتبات المطلوبة: pygame و python-chess
# التشغيل: py -3.13 chess_project_shapes_v2_commented.py
# ============================================================
# شرح: بداية أو نهاية وصف توثيقي يشرح وظيفة الجزء البرمجي.
"""
# شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
Chess Game - Player vs Player / Player vs AI
# شرح: بداية كتلة أو بنية تحكم تنظم تنفيذ الأوامر التالية.
Dependencies:
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    python -m pip install pygame python-chess

# شرح: بداية كتلة أو بنية تحكم تنظم تنفيذ الأوامر التالية.
Run:
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    py -3.13 chess_project_shapes_v2.py

# شرح: بداية كتلة أو بنية تحكم تنظم تنفيذ الأوامر التالية.
Features:
# شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
- Choose Player vs Player or Player vs AI from the start menu.
# شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
- Legal chess moves are handled by python-chess.
# شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
- Each piece displays its chess glyph and a capital letter (K, Q, R, B, N, P).
# شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
- Highlights selected pieces and legal destinations.
# شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
- Captured pieces, turn/status message, New Game, Flip Board, and Back to Menu.
# شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
- No undo button.
# شرح: بداية أو نهاية وصف توثيقي يشرح وظيفة الجزء البرمجي.
"""

# شرح: استيراد المكتبة اللازمة لاستخدام وظائفها في المشروع.
import random
# شرح: استيراد المكتبة اللازمة لاستخدام وظائفها في المشروع.
import pygame
# شرح: استيراد المكتبة اللازمة لاستخدام وظائفها في المشروع.
import chess

# شرح: تهيئة مكتبة Pygame قبل استخدام الرسوم والأحداث.
pygame.init()

# -------------------- Window and board settings --------------------

# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
WIDTH, HEIGHT = 1040, 760
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
BOARD_SIZE = 640
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
SQUARE_SIZE = BOARD_SIZE // 8
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
BOARD_X, BOARD_Y = 30, 75
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
PANEL_X = BOARD_X + BOARD_SIZE + 28
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
PANEL_W = WIDTH - PANEL_X - 24

# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# شرح: تحديد عنوان نافذة البرنامج.
pygame.display.set_caption("Chess Game")
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
CLOCK = pygame.time.Clock()

# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
BG = (25, 35, 49)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
PANEL = (36, 49, 66)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
WHITE_SQUARE = (238, 226, 202)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
DARK_SQUARE = (111, 143, 126)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
SELECTED = (247, 220, 91)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
LEGAL = (135, 190, 130)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
CAPTURE = (210, 105, 105)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
WHITE_TEXT = (247, 247, 242)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
MUTED_TEXT = (190, 201, 211)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
BUTTON = (53, 91, 77)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
BUTTON_HOVER = (70, 117, 97)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
BLUE_BUTTON = (58, 82, 119)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
BORDER = (76, 92, 108)

# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
FONT = pygame.font.SysFont("dejavusans", 24)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
SMALL_FONT = pygame.font.SysFont("dejavusans", 17)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
TINY_FONT = pygame.font.SysFont("dejavusans", 13)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
TITLE_FONT = pygame.font.SysFont("dejavusans", 38, bold=True)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
PIECE_FONT = pygame.font.SysFont("dejavusans", 48)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
LETTER_FONT = pygame.font.SysFont("arial", 15, bold=True)
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
BUTTON_FONT = pygame.font.SysFont("arial", 18, bold=True)

# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
PIECE_LETTERS = {
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.KING: "K",
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.QUEEN: "Q",
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.ROOK: "R",
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.BISHOP: "B",
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.KNIGHT: "N",
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.PAWN: "P",
# شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
}
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
PIECE_NAMES = {
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.KING: "King",
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.QUEEN: "Queen",
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.ROOK: "Rook",
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.BISHOP: "Bishop",
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.KNIGHT: "Knight",
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.PAWN: "Pawn",
# شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
}
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
PIECE_VALUES = {
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.PAWN: 100,
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.KNIGHT: 320,
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.BISHOP: 330,
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.ROOK: 500,
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.QUEEN: 900,
    # شرح: استخدام ثابت أو وظيفة من مكتبة python-chess الخاصة بقواعد الشطرنج.
    chess.KING: 20000,
# شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
}
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
GLYPHS = {
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    (chess.WHITE, chess.KING): "♔",
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    (chess.WHITE, chess.QUEEN): "♕",
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    (chess.WHITE, chess.ROOK): "♖",
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    (chess.WHITE, chess.BISHOP): "♗",
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    (chess.WHITE, chess.KNIGHT): "♘",
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    (chess.WHITE, chess.PAWN): "♙",
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    (chess.BLACK, chess.KING): "♚",
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    (chess.BLACK, chess.QUEEN): "♛",
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    (chess.BLACK, chess.ROOK): "♜",
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    (chess.BLACK, chess.BISHOP): "♝",
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    (chess.BLACK, chess.KNIGHT): "♞",
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    (chess.BLACK, chess.PAWN): "♟",
# شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
}

# -------------------- Shared game state --------------------

# شرح: إنشاء رقعة شطرنج جديدة بوضع البداية القياسي.
board = chess.Board()
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
game_mode = None            # "pvp" or "ai"
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
selected_square = None
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
legal_targets = []
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
flipped = False
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
message = "Choose a game mode to begin."
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
message_color = WHITE_TEXT
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
game_over_announced = False
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
last_move = None
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
captured_white = []         # Black pieces captured by White
# شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
captured_black = []         # White pieces captured by Black

# -------------------- Drawing helpers --------------------

# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def draw_text(text, x, y, font=FONT, color=WHITE_TEXT, surface=SCREEN):
    # شرح: إنشاء سطح مرئي أو صورة ليتم رسمها على الشاشة.
    image = font.render(str(text), True, color)
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    surface.blit(image, (x, y))
    # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
    return image.get_rect(topleft=(x, y))


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def draw_centered(text, rect, font=FONT, color=WHITE_TEXT):
    # شرح: إنشاء سطح مرئي أو صورة ليتم رسمها على الشاشة.
    image = font.render(str(text), True, color)
    # شرح: عرض الصورة أو النص في الموقع المحدد على الشاشة.
    SCREEN.blit(image, image.get_rect(center=rect.center))


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def draw_button(rect, text, color=BUTTON):
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    mouse_over = rect.collidepoint(pygame.mouse.get_pos())
    # شرح: رسم شكل أو عنصر مرئي داخل نافذة اللعبة.
    pygame.draw.rect(SCREEN, BUTTON_HOVER if mouse_over else color, rect, border_radius=10)
    # شرح: رسم شكل أو عنصر مرئي داخل نافذة اللعبة.
    pygame.draw.rect(SCREEN, BORDER, rect, width=1, border_radius=10)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_centered(text, rect, BUTTON_FONT, WHITE_TEXT)


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def reset_game(mode=None):
    # شرح: السماح للدالة بتعديل المتغير العام الموجود خارجها.
    global board, game_mode, selected_square, legal_targets, flipped
    # شرح: السماح للدالة بتعديل المتغير العام الموجود خارجها.
    global message, message_color, game_over_announced, last_move
    # شرح: السماح للدالة بتعديل المتغير العام الموجود خارجها.
    global captured_white, captured_black
    # شرح: إنشاء رقعة شطرنج جديدة بوضع البداية القياسي.
    board = chess.Board()
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    game_mode = mode
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    selected_square = None
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    legal_targets = []
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    flipped = False
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    message = "White to move."
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    message_color = WHITE_TEXT
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    game_over_announced = False
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    last_move = None
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    captured_white = []
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    captured_black = []


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def square_from_mouse(pos):
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    x, y = pos
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if not (BOARD_X <= x < BOARD_X + BOARD_SIZE and BOARD_Y <= y < BOARD_Y + BOARD_SIZE):
        # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
        return None
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    col = (x - BOARD_X) // SQUARE_SIZE
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    row = (y - BOARD_Y) // SQUARE_SIZE
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if flipped:
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        col = 7 - col
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        row = 7 - row
    # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
    return chess.square(col, 7 - row)


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def screen_coords(square):
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    file_index = chess.square_file(square)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    rank_index = chess.square_rank(square)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    col = file_index
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    row = 7 - rank_index
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if flipped:
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        col = 7 - col
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        row = 7 - row
    # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
    return BOARD_X + col * SQUARE_SIZE, BOARD_Y + row * SQUARE_SIZE


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def draw_piece(piece, rect):
    # شرح: بداية أو نهاية وصف توثيقي يشرح وظيفة الجزء البرمجي.
    """Render traditional chess-piece glyphs using Windows' Segoe UI Symbol font.

    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    This uses proper chess glyphs (king, queen, rook, bishop, knight, pawn)
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    rather than hand-drawn geometric approximations. Segoe UI Symbol is present
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    on standard Windows installations and supports the Unicode chess symbols.
    # شرح: بداية أو نهاية وصف توثيقي يشرح وظيفة الجزء البرمجي.
    """
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    glyph = GLYPHS[(piece.color, piece.piece_type)]
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    font = pygame.font.SysFont("Segoe UI Symbol", 57)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    cx, cy = rect.centerx, rect.centery - 2

    # Subtle shadow gives the piece more depth and keeps it clear on both squares.
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    shadow = font.render(glyph, True, (45, 48, 48))
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    shadow_rect = shadow.get_rect(center=(cx + 2, cy + 3))
    # شرح: عرض الصورة أو النص في الموقع المحدد على الشاشة.
    SCREEN.blit(shadow, shadow_rect)

    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    piece_color = (250, 248, 239) if piece.color == chess.WHITE else (32, 36, 40)
    # شرح: إنشاء سطح مرئي أو صورة ليتم رسمها على الشاشة.
    image = font.render(glyph, True, piece_color)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    image_rect = image.get_rect(center=(cx, cy))
    # شرح: عرض الصورة أو النص في الموقع المحدد على الشاشة.
    SCREEN.blit(image, image_rect)

    # Keep the requested capital abbreviation in a small contrasting badge.
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    letter = PIECE_LETTERS[piece.piece_type]
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    badge_color = (49, 64, 61) if piece.color == chess.WHITE else (239, 229, 204)
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    letter_color = (250, 248, 239) if piece.color == chess.WHITE else (32, 36, 40)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    badge = pygame.Rect(rect.right - 17, rect.bottom - 19, 15, 15)
    # شرح: رسم شكل أو عنصر مرئي داخل نافذة اللعبة.
    pygame.draw.circle(SCREEN, badge_color, badge.center, 8)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    letter_surface = pygame.font.SysFont("Arial", 10, bold=True).render(letter, True, letter_color)
    # شرح: عرض الصورة أو النص في الموقع المحدد على الشاشة.
    SCREEN.blit(letter_surface, letter_surface.get_rect(center=badge.center))


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def draw_board():
    # شرح: بدء حلقة تكرار لمعالجة كل عنصر في المجموعة.
    for row in range(8):
        # شرح: بدء حلقة تكرار لمعالجة كل عنصر في المجموعة.
        for col in range(8):
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            square = chess.square(col, 7 - row)
            # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
            if flipped:
                # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                square = chess.square(7 - col, row)

            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            x = BOARD_X + col * SQUARE_SIZE
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            y = BOARD_Y + row * SQUARE_SIZE
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
            # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
            color = WHITE_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE

            # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
            if square == selected_square:
                # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                color = SELECTED
            # شرح: فحص شرط بديل إذا لم يتحقق الشرط السابق.
            elif square in legal_targets:
                # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                color = CAPTURE if board.piece_at(square) else LEGAL
            # شرح: فحص شرط بديل إذا لم يتحقق الشرط السابق.
            elif last_move and square in (last_move.from_square, last_move.to_square):
                # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                color = tuple(min(255, c + 15) for c in color)

            # شرح: رسم شكل أو عنصر مرئي داخل نافذة اللعبة.
            pygame.draw.rect(SCREEN, color, rect)

            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            piece = board.piece_at(square)
            # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
            if piece:
                # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
                draw_piece(piece, rect)


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def draw_captured_section(title, pieces, x, y):
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_text(title, x, y, SMALL_FONT, MUTED_TEXT)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    y += 27
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if not pieces:
        # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
        draw_text("None", x, y, SMALL_FONT, (130, 145, 158))
        # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
        return
    # Keep rows within the side panel, even if many pieces are captured.
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    visible = pieces[-16:]
    # شرح: بدء حلقة تكرار لمعالجة كل عنصر في المجموعة.
    for idx, piece in enumerate(visible):
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        col = idx % 8
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        row = idx // 8
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        glyph = GLYPHS[(piece.color, piece.piece_type)]
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        glyph_surface = pygame.font.SysFont("Segoe UI Symbol", 24).render(glyph, True, WHITE_TEXT)
        # شرح: عرض الصورة أو النص في الموقع المحدد على الشاشة.
        SCREEN.blit(glyph_surface, (x + col * 27, y + row * 27))


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def game_status():
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if board.is_checkmate():
        # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
        winner = "Black" if board.turn == chess.WHITE else "White"
        # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
        return f"Checkmate! {winner} wins."
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if board.is_stalemate():
        # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
        return "Draw by stalemate."
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if board.is_insufficient_material():
        # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
        return "Draw: insufficient material."
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if board.is_seventyfive_moves():
        # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
        return "Draw by 75-move rule."
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if board.is_fivefold_repetition():
        # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
        return "Draw by repetition."
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    turn = "White" if board.turn == chess.WHITE else "Black"
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if board.is_check():
        # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
        return f"{turn} to move — CHECK!"
    # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
    return f"{turn} to move."


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def draw_game():
    # شرح: ملء الشاشة بلون الخلفية لمسح الرسم السابق.
    SCREEN.fill(BG)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_text("CHESS GAME", BOARD_X, 20, TITLE_FONT)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_text("Player vs Player" if game_mode == "pvp" else "Player vs AI",
              # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
              PANEL_X, 30, SMALL_FONT, MUTED_TEXT)

    # شرح: رسم شكل أو عنصر مرئي داخل نافذة اللعبة.
    pygame.draw.rect(SCREEN, PANEL,
                     # شرح: إنشاء مستطيل يحدد موقع وحجم عنصر في الواجهة.
                     pygame.Rect(PANEL_X - 10, BOARD_Y, PANEL_W + 20, BOARD_SIZE),
                     # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                     border_radius=14)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_board()

    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    status = game_status()
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_text("GAME STATUS", PANEL_X, 90, SMALL_FONT, MUTED_TEXT)
    # Wrap the status to fit the panel.
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if len(status) > 23:
        # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
        draw_text(status[:23], PANEL_X, 120, SMALL_FONT)
        # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
        draw_text(status[23:], PANEL_X, 143, SMALL_FONT)
    # شرح: تنفيذ البديل عندما لا يتحقق أي شرط سابق.
    else:
        # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
        draw_text(status, PANEL_X, 120, SMALL_FONT)

    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_text("CAPTURED BY WHITE", PANEL_X, 195, SMALL_FONT, MUTED_TEXT)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_captured_section("", captured_white, PANEL_X, 220)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_text("CAPTURED BY BLACK", PANEL_X, 290, SMALL_FONT, MUTED_TEXT)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_captured_section("", captured_black, PANEL_X, 315)

    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_text("PIECE KEY", PANEL_X, 395, SMALL_FONT, MUTED_TEXT)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_text("K King   Q Queen", PANEL_X, 423, SMALL_FONT)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_text("R Rook   B Bishop", PANEL_X, 450, SMALL_FONT)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_text("N Knight   P Pawn", PANEL_X, 477, SMALL_FONT)

    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    new_rect = pygame.Rect(PANEL_X, 535, PANEL_W, 42)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    flip_rect = pygame.Rect(PANEL_X, 587, PANEL_W, 42)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    menu_rect = pygame.Rect(PANEL_X, 639, PANEL_W, 42)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_button(new_rect, "New Game")
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_button(flip_rect, "Flip Board", BLUE_BUTTON)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_button(menu_rect, "Back to Menu", BLUE_BUTTON)

    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if message and message != status:
        # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
        draw_text(message[:31], PANEL_X, 505, TINY_FONT, message_color)

    # شرح: تحديث النافذة لإظهار الرسم الجديد.
    pygame.display.flip()
    # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
    return new_rect, flip_rect, menu_rect


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def draw_menu():
    # شرح: ملء الشاشة بلون الخلفية لمسح الرسم السابق.
    SCREEN.fill(BG)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    title = TITLE_FONT.render("CHESS GAME", True, WHITE_TEXT)
    # شرح: عرض الصورة أو النص في الموقع المحدد على الشاشة.
    SCREEN.blit(title, title.get_rect(center=(WIDTH // 2, 150)))
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    subtitle = FONT.render("Choose how you want to play", True, MUTED_TEXT)
    # شرح: عرض الصورة أو النص في الموقع المحدد على الشاشة.
    SCREEN.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 215)))

    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    pvp_rect = pygame.Rect(WIDTH // 2 - 190, 300, 380, 70)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    ai_rect = pygame.Rect(WIDTH // 2 - 190, 400, 380, 70)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    quit_rect = pygame.Rect(WIDTH // 2 - 190, 500, 380, 55)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_button(pvp_rect, "Player vs Player")
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_button(ai_rect, "Player vs AI", BLUE_BUTTON)
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    draw_button(quit_rect, "Quit", (91, 62, 66))
    # شرح: تحديث النافذة لإظهار الرسم الجديد.
    pygame.display.flip()
    # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
    return pvp_rect, ai_rect, quit_rect


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def choose_ai_move():
    # شرح: بداية أو نهاية وصف توثيقي يشرح وظيفة الجزء البرمجي.
    """Simple one-ply chess AI: prefer captures, material gain, checks and promotion."""
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    legal_moves = list(board.legal_moves)
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if not legal_moves:
        # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
        return None

    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    scored = []
    # شرح: بدء حلقة تكرار لمعالجة كل عنصر في المجموعة.
    for move in legal_moves:
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        score = random.uniform(0, 8)

        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        captured_piece = board.piece_at(move.to_square)
        # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
        if board.is_en_passant(move):
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            score += PIECE_VALUES[chess.PAWN] + 30
        # شرح: فحص شرط بديل إذا لم يتحقق الشرط السابق.
        elif captured_piece:
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            attacker = board.piece_at(move.from_square)
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            score += PIECE_VALUES[captured_piece.piece_type] - (
                # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
                PIECE_VALUES[attacker.piece_type] * 0.08 if attacker else 0
            # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
            )

        # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
        if move.promotion:
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            score += PIECE_VALUES.get(move.promotion, 0) + 500

        # شرح: تنفيذ النقلة على الرقعة وتحديث حالة اللعبة.
        board.push(move)
        # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
        if board.is_checkmate():
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            score += 100000
        # شرح: فحص شرط بديل إذا لم يتحقق الشرط السابق.
        elif board.is_check():
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            score += 35
        # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
        if board.is_stalemate():
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            score -= 500
        # شرح: التراجع عن آخر نقلة تجريبية وإرجاع الرقعة لحالتها السابقة.
        board.pop()

        # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
        scored.append((score, move))

    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    best_score = max(item[0] for item in scored)
    # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
    best_moves = [move for score, move in scored if score >= best_score - 10]
    # شرح: إرجاع النتيجة إلى المكان الذي استدعى الدالة.
    return random.choice(best_moves)


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def record_capture(move, moving_color):
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    captured = board.piece_at(move.to_square)
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if board.is_en_passant(move):
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        captured = chess.Piece(chess.PAWN, not moving_color)
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if captured:
        # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
        if moving_color == chess.WHITE:
            # شرح: تنفيذ إجراء أو تحديث قيمة مرتبطة بحالة اللعبة.
            captured_white.append(captured)
        # شرح: تنفيذ البديل عندما لا يتحقق أي شرط سابق.
        else:
            # شرح: تنفيذ إجراء أو تحديث قيمة مرتبطة بحالة اللعبة.
            captured_black.append(captured)


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def make_move(move):
    # شرح: السماح للدالة بتعديل المتغير العام الموجود خارجها.
    global selected_square, legal_targets, last_move, message, message_color
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    moving_color = board.turn
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    record_capture(move, moving_color)
    # شرح: تنفيذ النقلة على الرقعة وتحديث حالة اللعبة.
    board.push(move)
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    last_move = move
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    selected_square = None
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    legal_targets = []
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    message = ""
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    message_color = WHITE_TEXT


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def on_board_click(pos):
    # شرح: السماح للدالة بتعديل المتغير العام الموجود خارجها.
    global selected_square, legal_targets, message, message_color
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if board.is_game_over():
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        message = game_status()
        # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
        return

    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    square = square_from_mouse(pos)
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if square is None:
        # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
        return

    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    piece = board.piece_at(square)
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if selected_square is None:
        # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
        if piece and piece.color == board.turn:
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            selected_square = square
            # شرح: تحديث حالة اللعبة أو قيمة تستخدمها الواجهة.
            legal_targets = [m.to_square for m in board.legal_moves if m.from_square == square]
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            message = ""
        # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
        return

    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if square == selected_square:
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        selected_square = None
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        legal_targets = []
        # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
        return

    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if piece and piece.color == board.turn:
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        selected_square = square
        # شرح: تحديث حالة اللعبة أو قيمة تستخدمها الواجهة.
        legal_targets = [m.to_square for m in board.legal_moves if m.from_square == square]
        # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
        return

    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    candidates = [m for m in board.legal_moves
                  # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
                  if m.from_square == selected_square and m.to_square == square]
    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
    if candidates:
        # شرح: تنفيذ التعليمة ضمن تسلسل عمل البرنامج.
        move = next((m for m in candidates if m.promotion == chess.QUEEN), candidates[0])
        # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
        make_move(move)
    # شرح: تنفيذ البديل عندما لا يتحقق أي شرط سابق.
    else:
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        message = "Illegal move: choose a highlighted square."
        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
        message_color = (255, 180, 160)


# شرح: تعريف دالة لتنفيذ مهمة محددة عند استدعائها.
def main():
    # شرح: السماح للدالة بتعديل المتغير العام الموجود خارجها.
    global flipped, selected_square, legal_targets, message
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    running = True
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    in_menu = True
    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
    buttons = None

    # شرح: تكرار الأوامر ما دام الشرط صحيحاً.
    while running:
        # شرح: تنظيم سرعة تحديث الحلقة لتكون بحد أقصى 60 إطاراً في الثانية.
        CLOCK.tick(60)

        # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
        if in_menu:
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            pvp_rect, ai_rect, quit_rect = draw_menu()
        # شرح: تنفيذ البديل عندما لا يتحقق أي شرط سابق.
        else:
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            new_rect, flip_rect, menu_rect = draw_game()
            # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
            buttons = (new_rect, flip_rect, menu_rect)

            # AI plays as Black. The human always plays White in this mode.
            # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
            if game_mode == "ai" and board.turn == chess.BLACK and not board.is_game_over():
                # شرح: إيقاف قصير ومقصود قبل تنفيذ حركة الذكاء الاصطناعي.
                pygame.time.delay(300)
                # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                ai_move = choose_ai_move()
                # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
                if ai_move:
                    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
                    make_move(ai_move)

        # شرح: بدء حلقة تكرار لمعالجة كل عنصر في المجموعة.
        for event in pygame.event.get():
            # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
            if event.type == pygame.QUIT:
                # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                running = False

            # شرح: فحص شرط بديل إذا لم يتحقق الشرط السابق.
            elif event.type == pygame.KEYDOWN:
                # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
                if event.key == pygame.K_ESCAPE:
                    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
                    if in_menu:
                        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                        running = False
                    # شرح: تنفيذ البديل عندما لا يتحقق أي شرط سابق.
                    else:
                        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                        in_menu = True
                        # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
                        reset_game(None)

            # شرح: فحص شرط بديل إذا لم يتحقق الشرط السابق.
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                pos = event.pos
                # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
                if in_menu:
                    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
                    if pvp_rect.collidepoint(pos):
                        # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
                        reset_game("pvp")
                        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                        in_menu = False
                    # شرح: فحص شرط بديل إذا لم يتحقق الشرط السابق.
                    elif ai_rect.collidepoint(pos):
                        # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
                        reset_game("ai")
                        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                        in_menu = False
                    # شرح: فحص شرط بديل إذا لم يتحقق الشرط السابق.
                    elif quit_rect.collidepoint(pos):
                        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                        running = False
                # شرح: تنفيذ البديل عندما لا يتحقق أي شرط سابق.
                else:
                    # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                    new_rect, flip_rect, menu_rect = buttons
                    # شرح: فحص الشرط؛ ينفذ الجزء التالي إذا كانت النتيجة صحيحة.
                    if new_rect.collidepoint(pos):
                        # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
                        reset_game(game_mode)
                    # شرح: فحص شرط بديل إذا لم يتحقق الشرط السابق.
                    elif flip_rect.collidepoint(pos):
                        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                        flipped = not flipped
                        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                        selected_square = None
                        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                        legal_targets = []
                    # شرح: فحص شرط بديل إذا لم يتحقق الشرط السابق.
                    elif menu_rect.collidepoint(pos):
                        # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
                        reset_game(None)
                        # شرح: تخزين قيمة أو نتيجة في متغير لاستخدامها لاحقاً.
                        in_menu = True
                    # شرح: فحص شرط بديل إذا لم يتحقق الشرط السابق.
                    elif game_mode == "pvp" or board.turn == chess.WHITE:
                        # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
                        on_board_click(pos)

    # شرح: إغلاق Pygame وتحرير موارده عند إنهاء البرنامج.
    pygame.quit()


# شرح: تشغيل الدالة الرئيسية فقط عند تشغيل هذا الملف مباشرة.
if __name__ == "__main__":
    # شرح: استدعاء دالة لتنفيذ المهمة الموضحة باسمها.
    main()
