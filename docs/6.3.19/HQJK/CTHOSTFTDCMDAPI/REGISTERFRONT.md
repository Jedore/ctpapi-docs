<p>设置交易托管系统的网络通讯地址，交易托管系统拥有多个通信地址，用户可以注册一个或多个地址。如果注册多个地址会随机选择一个尝试连接。</p>
<span class="anchor" id="91d442bb-2f26-4a60-9223-d2e1e4e4007c"></span>
## 1.函数原型
<p>virtual void RegisterFront(char *pszFrontAddress) = 0;</p>
<span class="anchor" id="29df8815-69a8-4c73-9c50-f7fa0456cf7f"></span>
## 2.参数
<p>pszFrontAddress：指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”如：”tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表行情端口号。</p>
<p>SSL前置格式：ssl://192.168.0.1:41205</p>
<p>TCP前置格式：tcp://192.168.0.1:41205</p>
</blockquote>
<span class="anchor" id="31405367-345b-452d-82e1-bb41eaac05de"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1000a077-3e6b-42bc-b151-e8560d843ba1"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
//此处注册多个前置，连接的时候会随机选择一个
pUserMdApi-&gt;RegisterFront(“tcp://192.168.0.1:41213”); 
pUserMdApi-&gt;RegisterFront(“tcp://192.168.0.2:41213”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="97a4fde1-d543-4b9c-96ff-ec037c9a2162"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">如果我注册了多个前置，会选择一个最优的前置进行连接吗？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>不会，完全是随机的。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
