<p>用户口令更新请求，对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPUSERPASSWORDUPDATE/">OnRspUserPasswordUpdate</a>。</p>
<span class="anchor" id="0b924810-e9d6-4cae-baa3-ee0b7e94f0e6"></span>
## 1.函数原型
<p>virtual int ReqUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID) = 0;</p>
<span class="anchor" id="fb8f964b-5fc6-4586-a372-7a2ff5466e78"></span>
## 2.参数
<p>pUserPasswordUpdate：用户口令变更</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPasswordType</td>
<td style="TEXT-ALIGN: left;">OldPassword</td>
<td style="TEXT-ALIGN: left;">原来的口令</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPasswordType</td>
<td style="TEXT-ALIGN: left;">NewPassword</td>
<td style="TEXT-ALIGN: left;">新的口令</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
</table>
<p>NewPassword：新密码需要符合复杂度要求，不然修改失败。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="1a09a01c-1a6d-46d3-821a-568fb3a8df37"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1566b2b4-68b8-4a22-82f2-b51dd458914d"></span>
## 4.调用示例
<pre><code>CThostFtdcUserPasswordUpdateField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.UserID, "1000001");
strcpy_s(a.OldPassword, "123456");
strcpy_s(a.NewPassword, "666666");
m_pUserApi-&gt;ReqUserPasswordUpdate(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="acec14c7-da93-420c-ad40-20386b67177a"></span>
## 5.FAQ
<p>无</p>
