<p>请求查询客户通知</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYNOTICE/">OnRspQryNotice</a></p>
<span class="anchor" id="91369274-9db8-4f32-b756-594f5d61eb22"></span>
## 1.函数原型
<p>virtual int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) = 0;</p>
<span class="anchor" id="67574c29-f4db-415c-8f8d-c66ab851142f"></span>
## 2.参数
<p>pQryNotice：查询客户通知</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="6d83c2ef-24d5-438d-aba4-77f5b81408b4"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="31416456-0eea-4f18-a73b-752552f6f7e2"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="1d822f44-8dc6-437b-a0ec-0857e41fceac"></span>
## 5.FAQ
<p>无</p>
