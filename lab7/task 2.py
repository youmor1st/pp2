import pygame
import os

pygame.init()

monitor = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Music Player")

music_dir = "music"
music_files = os.listdir(music_dir)

font = pygame.font.SysFont("candara", 48)

current_song = 0
paused_pos = 0
old_song_time = 0
is_playing = False
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song]))

def play_song():
    global is_playing
    pygame.mixer.music.play(start=paused_pos)
    is_playing = True

def pause_song():
    global is_playing, paused_pos, old_song_time
    pygame.mixer.music.pause()
    paused_pos = pygame.mixer.music.get_pos() / 1000 + old_song_time
    old_song_time += pygame.mixer.music.get_pos() / 1000
    is_playing = False

def next_song():
    global current_song, is_playing
    current_song += 1
    if current_song >= len(music_files):
        current_song = 0
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song]))
    if is_playing:
        pygame.mixer.music.play()

def prev_song():
    global current_song, is_playing
    current_song -= 1
    if current_song < 0:
        current_song = len(music_files) - 1
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song]))
    if is_playing:
        pygame.mixer.music.play()

check = True
while check:

    pygame.display.update()
    monitor.fill((255, 255, 255))
    song_title = font.render(music_files[current_song], True, (0, 0, 0))
    monitor.blit(song_title, (0, 150))

    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()

        elif action.type == pygame.KEYDOWN:

            if action.key == pygame.K_SPACE:
                if is_playing:
                    pause_song()
                else:
                    play_song()

            elif action.key == pygame.K_LEFT:
                next_song()

            elif action.key == pygame.K_RIGHT:
                prev_song()