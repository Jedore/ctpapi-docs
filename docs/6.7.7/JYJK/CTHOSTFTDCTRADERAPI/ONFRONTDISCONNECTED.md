<p>当客户端与交易托管系统通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。自动重连地址，可能是原来注册的地址，也可能是系统支持的其它可用的通信地址，它由程序自动选择。</p>
<p>注:重连之后需要重新认证、登录</p>
<span class="anchor" id="937adb87-c06b-496a-9739-6b22f680d1a7"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDSPI/ONFRONTDISCONNECTED/">OnFrontDisconnected</a>(int nReason){};</p>
<span class="anchor" id="e5f07101-6afe-4b7a-bce4-bc06b71c3dc3"></span>
## 2.参数
<p>nReason：连接断开原因，注意该返回值为10进制数，所以要转换成16进制再对照下列错误号。</p>
<p><span alt="" id="anchor-id-01"></span> </p>
<blockquote>
<p>0x1001（4097） 网络读失败。recv=-1</p>
<p>0x1002（4098） 网络写失败。send=-1</p>
<p>0x2001（8193） 接收心跳超时。前置每53s会给一个心跳报文给api，如果api超过120s未收到任何新数据，则认为网络异常，断开连接</p>
<p>0x2002（8194） 发送心跳失败。api每15s会发送一个心跳报文给前置，如果api检测到超过40s没发送过任何新数据，则认为网络异常，断开连接</p>
<p>0x2003 收到错误报文</p>
</blockquote>
<span class="anchor" id="3981f78d-ea3c-4acc-a578-9e985b478edf"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c38c569b-de63-41d5-af0d-71123b31c093"></span>
## 4.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">为何有的时候密码错误或者终端认证失败会触发<a href="../../../HQJK/CTHOSTFTDCMDSPI/ONFRONTDISCONNECTED/">OnFrontDisconnected</a>？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>可能是因为CTP交易前置设置了ConnectFrq（每秒连接数）参数。设置该参数后，每秒连接数超过阈值就会拒绝API的连接，触发断线。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
