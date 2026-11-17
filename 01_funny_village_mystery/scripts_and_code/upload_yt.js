async function run() {
  const res = await fetch('http://localhost:9222/json');
  const pages = await res.json();
  const ytPage = pages.find(p => p.url && p.url.includes('studio.youtube.com'));
  if (!ytPage) {
    console.error('YouTube Studio tab not found');
    process.exit(1);
  }
  console.log('Found YouTube Studio tab:', ytPage.title);

  const ws = new WebSocket(ytPage.webSocketDebuggerUrl);
  ws.onopen = () => {
    ws.send(JSON.stringify({ id: 1, method: 'DOM.getDocument' }));
  };
  ws.onmessage = (e) => {
    const data = JSON.parse(e.data);
    if (data.id === 1) {
      ws.send(JSON.stringify({
        id: 2,
        method: 'DOM.querySelector',
        params: { nodeId: data.result.root.nodeId, selector: 'input[type="file"]' }
      }));
    } else if (data.id === 2) {
      console.log('File input nodeId:', data.result.nodeId);
      ws.send(JSON.stringify({
        id: 3,
        method: 'DOM.setFileInputFiles',
        params: {
          files: ['F:\\YouTube\\funny_village_mystery\\100_percent_real_motion_cartoon_movie.mp4'],
          nodeId: data.result.nodeId
        }
      }));
    } else if (data.id === 3) {
      console.log('File set successfully:', data);
      setTimeout(() => process.exit(0), 1000);
    }
  };
  ws.onerror = (err) => console.error('WS error:', err);
}
run();

