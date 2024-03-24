<p>当客户端与交易托管系统通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。自动重连地址，可能是原来注册的地址，也可能是系统支持的其它可用的通信地址，它由程序自动选择。</p>
<p>注:重连之后需要重新认证、登录</p>
<span class="anchor" id="e97e541b-33de-4490-9a92-b48a51090e82"></span>
## 1.函数原型
<p>virtual void OnFrontDisconnected(int nReason){};</p>
<span class="anchor" id="4fc3368c-8360-47d0-9d5a-17f6ef5ee7cf"></span>
## 2.参数
<p>nReason：连接断开原因，注意该返回值为10进制数，所以要转换成16进制再对照下列错误号。</p>
<blockquote>
<p>0x1001 网络读失败</p>
<p>0x1002 网络写失败</p>
<p>0x2001 接收心跳超时</p>
<p>0x2002 发送心跳失败</p>
<p>0x2003 收到错误报文</p>
</blockquote>
<span class="anchor" id="7fd88b45-d544-4e6b-88b2-589fffa8a909"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="571a2e45-cd15-49d0-b179-33e907d42986"></span>
## 4.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">为何有的时候密码错误或者终端认证失败会触发OnFrontDisconnected？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>可能是因为CTP交易前置设置了ConnectFrq（每秒连接数）参数。设置该参数后，每秒连接数超过阈值就会拒绝API的连接，触发断线。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
