<p>设置交易托管系统的网络通讯地址，交易托管系统拥有多个通信地址，但用户只需要选择一个通信地址。</p>
<p>也可以通过多次调用的方式注册不同的前置地址实现冗余。当交易系统断开连接时会自动从注册的地址池中随机选择一个尝试连接。</p>
<span class="anchor" id="b0371747-d891-4da2-9e73-e253d78c7d82"></span>
## 1.函数原型
<p>virtual void RegisterFront(char *pszFrontAddress) = 0;</p>
<span class="anchor" id="a18c2d6f-5083-4948-8c41-8f606267f3da"></span>
## 2.参数
<p>pszFrontAddress：指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表交易端口号。</p>
<p>SSL前置格式：ssl://192.168.0.1:41205</p>
<p>TCP前置格式：tcp://192.168.0.1:41205</p>
</blockquote>
<span class="anchor" id="9262d929-b024-402f-83c2-f84afec80d7c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c1234fa6-7ce1-4b18-9b37-d3efcc8747c7"></span>
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
<span class="anchor" id="8fbbb805-eab3-445d-8e7c-639bd8ada878"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“CTP:无此功能”是什么错？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>端口如果填写错误，例如交易和行情写反，则会报。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
