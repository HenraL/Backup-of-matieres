# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Pour tester.py'],
             pathex=['C:\\Users\\Henry PC\\Documents\\001 Github prog Sharing\\Backup-of-matiere\\files\\Matières\\NSI\\T1\\.py\\Discord_i_t_t_a_c_i_g\\files_in_dev\\get_windows_info'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Pour tester',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
