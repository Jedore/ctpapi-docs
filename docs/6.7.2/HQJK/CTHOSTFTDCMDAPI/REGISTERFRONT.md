<p>设置交易托管系统的网络通讯地址，交易托管系统拥有多个通信地址，用户可以注册一个或多个地址。如果注册多个地址则使用最先建立TCP连接的地址。</p>
<span class="anchor" id="bd248b78-e438-4f49-8edb-387eff7960d2"></span>
## 1.函数原型
<p>virtual void RegisterFront(char *pszFrontAddress) = 0;</p>
<span class="anchor" id="b1836f64-b2dd-4979-bc1f-bfab3ab64eb0"></span>
## 2.参数
<p>pszFrontAddress：指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”如：”tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表行情端口号。</p>
<p>SSL前置格式：ssl://192.168.0.1:41205</p>
<p>TCP前置IPv4格式：tcp://192.168.0.1:41205</p>
<p>TCP前置IPv6格式：tcp6://fe80::20f8:aa9b:7d59:887d:35001</p>
</blockquote>
<span class="anchor" id="2fbd94f3-394b-4ad1-a467-ac46f2f15cdc"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2600685f-1254-493d-82d9-5dd9b9377c56"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
//此处注册多个前置
pUserMdApi-&gt;RegisterFront(“tcp://192.168.0.1:41213”); 
pUserMdApi-&gt;RegisterFront(“tcp://192.168.0.2:41213”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="9c72cdd6-a9fd-40bf-8eba-5c551cede402"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">如果我注册了多个前置，会选择一个最优的前置进行连接吗？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>会以最先建立TCP连接的地址作为当前连接地址进行连接。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
