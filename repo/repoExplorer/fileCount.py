from pathlib import Path, PurePosixPath

TotalPercent = 100
count = {}



extensionMap = {
    ".py": "Python",
    ".pyc": "Python Compiled",
    ".pyo": "Python Optimized",
    ".pyz": "Python Zip App",

    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".js": "JavaScript",
    ".jsx": "React JavaScript",
    ".ts": "TypeScript",
    ".tsx": "React TypeScript",
    
    ".json": "JSON",
    ".xml": "XML",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".toml": "TOML",
    ".ini": "INI Config",
    ".cfg": "Config",
    ".conf": "Config",
    ".env": "Environment File",
    ".lock": "Lock File",
    
    ".md": "Markdown",
    ".rst": "reStructuredText",
    ".txt": "Text",
    ".pdf": "PDF",

    ".c": "C",
    ".h": "C Header",
    ".cpp": "C++",
    ".hpp": "C++ Header",

    ".java": "Java",
    ".class": "Java Bytecode",
    ".jar": "Java Archive",

    ".sh": "Shell Script",
    ".bash": "Bash Script",
    ".zsh": "Zsh Script",
    ".bat": "Batch Script",

    ".png": "PNG Image",
    ".jpg": "JPEG Image",
    ".jpeg": "JPEG Image",
    ".gif": "GIF Image",
    ".svg": "SVG Image",
    ".ico": "Icon",

    ".zip": "ZIP Archive",
    ".tar": "TAR Archive",
    ".gz": "GZip Archive",
    ".tgz": "TGZ Archive",
    ".rar": "RAR Archive",
    ".7z": "7Zip Archive",

    ".csv": "CSV",
    ".xlsx": "Excel Spreadsheet",
    ".docx": "Word Document",
    ".pptx": "PowerPoint",

    ".whl": "Python Wheel",
    ".gem": "Ruby Gem",
    ".map": "Source Map",

    ".LICENSE": "License File",
    ".NOTICE": "Notice File",
    ".ABOUT": "About File",
    ".in": "Input File",
    ".d": "Dependency File"
}
def counter(repoPath):
    p = Path(repoPath)
    folders = [x for x in p.iterdir() if x.is_dir()]
    allFiles = list(p.glob('**/*.*'))
    
    for a in allFiles:
        skip = False

        for b in folders:
            if b.name.startswith('.') and str(a).startswith(str(b)):
                skip = True
        if skip:
            continue
        if "__pycache__" in str(a):
            continue
        if a.name.startswith('.'):
            continue
        suffix = a.suffix
        # print(allExtensions)

        category = extensionMap.get(suffix, "Unknown Files")
        # print(category)
        suffix = a.suffix
        if suffix in count:
            count[suffix] += 1
        else:
            count[suffix] = 1
    total_files = sum(count.values())
    
    sorted_counts = sorted(count.items(), key=lambda x: x[1], reverse=True)
    for c,values in sorted_counts:
        category = extensionMap.get(c, "Unknown ")
        percentage = round((values / total_files) * 100, 1)
        
        print(f"| {category:<20} -> {values:<5} files = {percentage:<5}% |")
    print("=> Total no of files: ", total_files )
