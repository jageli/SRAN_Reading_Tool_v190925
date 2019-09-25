# -*- mode: python -*-

block_cipher = None


a = Analysis(['main6.py'],
             pathex=['C:\\Users\\J7LI\\OneDrive - Nokia\\python\\python\\mypy37-32\\SRAN_Reading\\SRAN_Reading_ToolV2\\TDD_mod','C:\\Users\\J7LI\\OneDrive - Nokia\\python\\python\\mypy37-32\\SRAN_Reading\\SRAN_Reading_ToolV2\\SRAN_mod','C:\\Users\\J7LI\\OneDrive - Nokia\\python\\python\\mypy37-32\\SRAN_Reading\\SRAN_Reading_ToolV2'],
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
          name='SRAN_Reading_ToolV2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='icon\\icon.ico')
