<p>请求查询客户通知</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYNOTICE/">OnRspQryNotice</a></p>
<span class="anchor" id="c57b338b-c9d5-4216-94e0-dd538f5c920d"></span>
## 1.函数原型
<p>virtual int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) = 0;</p>
<span class="anchor" id="7aa7fc73-d3c8-48f6-9b25-bb5c5cbfe03d"></span>
## 2.参数
<p>pQryNotice：查询客户通知</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="eb91c0c9-c99b-463d-885a-0952925cde69"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1db06d0d-db6f-421a-b216-b3ef7903912a"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="fa90318a-1952-45a8-8b64-688e950b1059"></span>
## 5.FAQ
<p>无</p>
