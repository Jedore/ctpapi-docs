<p>请求查询客户通知</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYNOTICE/">OnRspQryNotice</a></p>
<span class="anchor" id="5be01583-4626-4142-baa0-02d0025232fb"></span>
## 1.函数原型
<p>virtual int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) = 0;</p>
<span class="anchor" id="8ff1d296-32aa-40d2-af0c-cb16b216fee2"></span>
## 2.参数
<p>pQryNotice：查询客户通知</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="6206e758-3ba7-459a-9ac8-a5f1e717c1bb"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c59ba220-096e-4ec8-80eb-8622737f5261"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="5279faf0-9f6f-4a2c-a6b2-93b4f843b20e"></span>
## 5.FAQ
<p>无</p>
