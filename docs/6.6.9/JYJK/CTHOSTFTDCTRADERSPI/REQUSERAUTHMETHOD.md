<p>查询用户当前支持的认证模式，暂不支持</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPUSERAUTHMETHOD/">OnRspUserAuthMethod</a></p>
<span class="anchor" id="b7d68cb1-fce5-4141-a6a9-d794eaf3a8cc"></span>
## 1.函数原型
<p>virtual int ReqUserAuthMethod(CThostFtdcReqUserAuthMethodField *pReqUserAuthMethod, int nRequestID) = 0;</p>
<span class="anchor" id="81cba318-f018-42e0-864f-59db64b36806"></span>
## 2.参数
<p>pReqUserAuthMethod：用户发出获取安全安全登陆方法请求</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcDateType</td>
<td style="TEXT-ALIGN: left;">TradingDay</td>
<td style="TEXT-ALIGN: left;">交易日</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="22f0f76c-6e4d-4628-9e24-d7072941eeb2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2de94574-8607-4f76-a072-9edc74ad4626"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="718821f2-eb7f-427b-a21e-575382728874"></span>
## 5.FAQ
<p>无</p>
