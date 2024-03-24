<p>请求查询客户通知</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYNOTICE/">OnRspQryNotice</a></p>
<span class="anchor" id="2ee66eb7-0077-4982-aafc-68782dad8e9f"></span>
## 1.函数原型
<p>virtual int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) = 0;</p>
<span class="anchor" id="fe11327e-b26e-4678-bc5d-2e48d5f7a799"></span>
## 2.参数
<p>pQryNotice：查询客户通知</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="32f1f14a-0f94-489d-8182-97e5e05218e3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1981b02d-05f6-43e1-adbb-ddad99c3a80f"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="0fde2685-d37f-4dbc-a4eb-962481e60209"></span>
## 5.FAQ
<p>无</p>
