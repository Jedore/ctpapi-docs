<p>注册名字服务器用户信息，调用<a href="../../../HQJK/CTHOSTFTDCMDAPI/REGISTERNAMESERVER/">RegisterNameServer</a>前需要先使用RegisterFensUserInfo设置登录模式。</p>
<p>详见<a href="../../../QTYWGZ/FENS/">fens连接说明</a></p>
<span class="anchor" id="7f183937-750f-43d1-9bb8-5e38e63ce8ad"></span>
## 1.函数原型
<p>virtual void RegisterFensUserInfo(CThostFtdcFensUserInfoField * pFensUserInfo) = 0;</p>
<span class="anchor" id="710745fd-86ef-423b-bae4-9cceef69380f"></span>
## 2.参数
<p>CThostFtdcFensUserInfoField：Fens用户信息</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcLoginModeType</td>
<td style="TEXT-ALIGN: left;">LoginMode</td>
<td style="TEXT-ALIGN: left;">登录模式</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
</table>
<p>LoginMode：填写<code>THOST_FTDC_LM_Trade</code></p>
<span class="anchor" id="75b81606-b0fd-452a-a4f4-bee3e81f441b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e944888e-4999-4911-8789-4f70666b9bd0"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
printf(pUserApi-&gt;GetApiVersion());
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
CThostFtdcFensUserInfoField pFensUserInfo = { 0 };
strcpy_s(pFensUserInfo.BrokerID, "9999");
strcpy_s(pFensUserInfo.UserID, "1000001");
pFensUserInfo.LoginMode = THOST_FTDC_LM_Trade;
pUserApi-&gt;RegisterFensUserInfo(&amp;pFensUserInfo);
pUserApi-&gt; RegisterNameServer("tcp://127.0.0.1:41205");
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="95da6742-41ac-4026-8aba-6388323ed7a9"></span>
## 5.FAQ
<p>无</p>
