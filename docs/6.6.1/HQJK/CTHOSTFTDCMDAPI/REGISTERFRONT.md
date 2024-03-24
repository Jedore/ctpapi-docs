<p>设置交易托管系统的网络通讯地址，交易托管系统拥有多个通信地址，用户可以注册一个或多个地址。如果注册多个地址则使用最先建立TCP连接的地址。</p>
<span class="anchor" id="11b9b4f8-458e-47fa-9d3e-311e2204d74e"></span>
## 1.函数原型
<p>virtual void <a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERFRONT/">RegisterFront</a>(char *pszFrontAddress) = 0;</p>
<span class="anchor" id="ba0f5176-1e8c-4c5d-8bb3-ad485edb44e7"></span>
## 2.参数
<p>pszFrontAddress：指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”如：”tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表行情端口号。</p>
<p>SSL前置格式：ssl://192.168.0.1:41205</p>
<p>TCP前置IPv4格式：tcp://192.168.0.1:41205</p>
<p>TCP前置IPv6格式：tcp6://fe80::20f8:aa9b:7d59:887d:35001</p>
</blockquote>
<span class="anchor" id="7a5b7605-1df9-4f95-9dcb-357f0c3a043f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="550b6d52-0978-4a65-bb12-6bc5121e1602"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
//此处注册多个前置
pUserMdApi-&gt;RegisterFront(“tcp://192.168.0.1:41213”); 
pUserMdApi-&gt;RegisterFront(“tcp://192.168.0.2:41213”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="384b82c5-da42-47d1-951f-cc212312f5bd"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">如果我注册了多个前置，会选择一个最优的前置进行连接吗？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>会以最先建立TCP连接的地址作为当前连接地址进行连接。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
