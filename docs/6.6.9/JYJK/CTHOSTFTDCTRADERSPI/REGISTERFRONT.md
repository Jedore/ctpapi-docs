<p>设置交易托管系统的网络通讯地址，交易托管系统拥有多个通信地址，但用户只需要选择一个通信地址。</p>
<p>也可以通过多次调用的方式注册不同的前置地址实现冗余。当交易系统断开连接时会自动从注册的地址池中择优选择一个建立连接。择优方式为以最先建立TCP连接的地址为连接地址。</p>
<span class="anchor" id="6b8f06f9-d6e7-4845-b562-f2d0bbfcdff6"></span>
## 1.函数原型
<p>virtual void RegisterFront(char *pszFrontAddress) = 0;</p>
<span class="anchor" id="381a1ead-8dd8-42de-9e1a-c96f5695b0fc"></span>
## 2.参数
<p>pszFrontAddress：指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表交易端口号。</p>
<p>SSL前置格式：ssl://192.168.0.1:41205</p>
<p>TCP前置IPv4格式：tcp://192.168.0.1:41205</p>
<p>TCP前置IPv6格式：tcp6://fe80::20f8:aa9b:7d59:887d:35001</p>
</blockquote>
<span class="anchor" id="20e4b86f-6363-468a-9b55-857958ed2ba2"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="002f5e2c-c757-4125-a837-0a872cf38a11"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow \\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESUME);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESUME);
//注册多个前置地址
pUserApi-&gt;RegisterFront(“tcp://192.168.1.10:51205”);
pUserApi-&gt;RegisterFront(“tcp://192.168.1.11:51205”);
pUserApi-&gt;RegisterFront(“tcp://192.168.1.12:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="741d1d4d-b431-460e-bf6d-c5c0dad7d6de"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“CTP:无此功能”是什么错？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>端口如果填写错误，例如交易和行情写反，则会报。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
