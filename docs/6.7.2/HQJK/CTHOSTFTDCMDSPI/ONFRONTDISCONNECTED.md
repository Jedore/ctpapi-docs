<p>当客户端与交易托管系统通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。自动重连地址，可能是原来注册的地址，也可能是系统支持的其它可用的通信地址，它由程序自动选择。</p>
<p>注:重连之后需要重新认证、登录</p>
<span class="anchor" id="26d08912-723d-4549-a287-089c1493c7a6"></span>
## 1.函数原型
<p>virtual void <a href="../../../JYJK/CTHOSTFTDCTRADERAPI/ONFRONTDISCONNECTED/">OnFrontDisconnected</a>(int nReason){};</p>
<span class="anchor" id="47559b3e-57c7-4b34-8b2e-261854a3ac52"></span>
## 2.参数
<p>nReason：连接断开原因，为10进制值，因此需要转成16进制后再参照下列代码：</p>
<blockquote>
<p>0x1001 网络读失败</p>
<p>0x1002 网络写失败</p>
<p>0x2001 接收心跳超时</p>
<p>0x2002 发送心跳失败</p>
<p>0x2003 收到错误报文</p>
</blockquote>
<span class="anchor" id="d1ba7347-c8b3-4a8b-9c57-bb179a7cd95d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ba57a1a1-c63f-4cb6-a28b-8e1814e5ee98"></span>
## 4.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">API每次断线都会自动重连，可以设置为不重连或者指定重连时间间隔吗？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>断线重连时间不可自定义，并且也无法通过参数设置来主动取消断线重连机制。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
