<p>注册名字服务器用户信息，调用RegisterNameServer前需要先使用RegisterFensUserInfo设置登录模式。</p>
<p>详见<a href="../../../QTYWGZ/FENS/">fens连接说明</a></p>
<span class="anchor" id="d2339f62-ebd9-4d2c-be2c-ba61a67bfa76"></span>
## 1.函数原型
<p>virtual void RegisterFensUserInfo(CThostFtdcFensUserInfoField * pFensUserInfo) = 0;</p>
<span class="anchor" id="41e4af05-facb-4106-b9f8-5ee7abc90d30"></span>
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
<span class="anchor" id="b27955be-30d2-48db-b3fb-1683ef54c67c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="350db77c-16f7-45f7-a71c-47f939aa7e79"></span>
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
<span class="anchor" id="197eb76e-8a9f-414b-80cd-5d3f71973779"></span>
## 5.FAQ
<p>无</p>
