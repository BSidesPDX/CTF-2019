if [[ "$EUID" -ne 0 ]]; then
    echo "[!] https://www.youtube.com/watch?v=InQiwMSXmwQ"
    echo "I thought for sure you'd trust us by now... https://www.youtube.com/watch?v=1zYWVHIS1i4"
    exit 1
fi

echo -e "Here's the flag...\n"
echo -e 'Flag: BSidesPDX{n3v3r_$ud0_(ur1_b4$h_1t5_r3411y_b4d}\n'
echo -e "But seriously, never do that again. Piping content from the internet directly to bash is a bad idea."