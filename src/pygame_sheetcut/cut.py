import pygame.surface, pygame.rect
from pygame.math import Vector2

def cut_grid(sheet: pygame.surface.Surface, rows: int, columns: int, scale: float=1.0) -> list:
    """cut_grid(sheet, rows, columns) -> list
    cut_grid(sheet, rows, columns, scale=1.0) -> list
    Splits a spritesheet into tiles, based on the number of rows and columns specified.
    Parameters:
        sheet (pygame.Surface): a pygame.Surface representing a spritesheet
        rows (int): the number of rows to split the sheet into
        columns (int): the number of columns to split the sheet into
        scale (float): (optional) a scale factor to apply to the returned tiles
    Returns: a list of tiles (pygame.Surface s) the sheet was split into.
    """
    if scale != 1.0:
        if scale == 2.0:
            sheet = pygame.transform.scale2x(sheet)
        else:
            sheet = pygame.transform.scale_by(sheet, scale)
    tile_width, tile_height = Vector2(sheet.get_size()) / Vector2(columns, rows).elementwise()
    tile_width, tile_height = int(tile_width), int(tile_height)
    tile_size = (tile_width, tile_height)
    frames = []
    for y in range(0, rows):
        for x in range(0, columns):
            rect = pygame.Rect((x*tile_width, y*tile_height), tile_size)
            subsurf = sheet.subsurface(rect)
            frames.append(subsurf)
    return frames

def cut_size(sheet: pygame.surface.Surface, tile_width: int, tile_height: int, scale: float=1.0) -> list:
    """cut_size(sheet, tile_width, tile_height) -> list
    cut_size(sheet, tile_width, tile_height, scale=1.0) -> list
    Splits a spritesheet into tiles, based on the tile size specified.
    Parameters:
        sheet (pygame.Surface): a pygame.Surface representing a spritesheet
        tile_width (int): the width, in pixels, of each tile
        tile_height (int): the height, in pixels, of each tile
        scale (float): (optional) a scale factor to apply to the returned tiles
    Returns: a list of tiles (pygame.Surface s) the sheet was split into.
    """
    if scale != 1.0:
        if scale == 2.0:
            sheet = pygame.transform.scale2x(sheet)
            tile_width *= 2
            tile_height *= 2
        else:
            sheet = pygame.transform.scale_by(sheet, scale)
            tile_width *= scale
            tile_height *= scale
    frames = []
    sheet_size = sheet.get_size()
    for y in range(0, sheet_size[1], tile_height):
        for x in range(0, sheet_size[0], tile_width):
            if x + tile_width > sheet_size[0]:
                w = sheet_size[0] - x
            else:
                w = tile_width
            if y + tile_height > sheet_size[1]:
                h = sheet_size[1] - y
            else:
                h = tile_height
            subsurf = sheet.subsurface(pygame.Rect((x, y), (w, h)))
            frames.append(subsurf)
    return subsurf