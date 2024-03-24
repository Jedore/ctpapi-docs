<p>查询用户当前支持的认证模式，暂不支持</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPUSERAUTHMETHOD/">OnRspUserAuthMethod</a></p>
<span class="anchor" id="5dd31177-3c21-4b77-9615-2de80c6db72e"></span>
## 1.函数原型
<p>virtual int ReqUserAuthMethod(CThostFtdcReqUserAuthMethodField *pReqUserAuthMethod, int nRequestID) = 0;</p>
<span class="anchor" id="9973dfff-a547-4925-8ac9-831d0fe903ef"></span>
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
<span class="anchor" id="bdccd8ee-27a4-45ee-bb0d-985241cd6b47"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c42ac0e2-e6a8-43d5-a92f-bee50ce29d53"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="e8a8bb44-b3f6-4acd-9b24-e65f19d50a6f"></span>
## 5.FAQ
<p>无</p>
