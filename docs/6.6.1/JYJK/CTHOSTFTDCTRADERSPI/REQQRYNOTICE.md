<p>请求查询客户通知</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYNOTICE/">OnRspQryNotice</a></p>
<span class="anchor" id="6f942e46-87d2-4b49-a3a7-a330400e8ed4"></span>
## 1.函数原型
<p>virtual int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) = 0;</p>
<span class="anchor" id="fdf86217-028c-4e38-aada-c67d3e9e9aaf"></span>
## 2.参数
<p>pQryNotice：查询客户通知</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="95e45145-e97b-43ad-9313-2f1a74ee2693"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0bd49c5d-8691-49dd-9c2d-ea494a6bbe3f"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="9d34ced6-51d7-4dfd-af5e-febf435fe7c5"></span>
## 5.FAQ
<p>无</p>
