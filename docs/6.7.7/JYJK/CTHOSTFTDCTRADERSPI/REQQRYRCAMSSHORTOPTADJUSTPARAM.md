<p>请求RCAMS空头期权风险调整参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSSHORTOPTADJUSTPARAM/">OnRspQryRCAMSShortOptAdjustParam</a></p>
<span class="anchor" id="0a102e49-46c2-44a7-97ed-2eee5d76c012"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSShortOptAdjustParam(CThostFtdcQryRCAMSShortOptAdjustParamField *pQryRCAMSShortOptAdjustParam, int nRequestID) = 0;</p>
<span class="anchor" id="ab29f499-2ec1-4cb7-bf66-28469f4ade80"></span>
## 2.参数
<p>pQryRCAMSShortOptAdjustParam：RCAMS空头期权风险调整参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProductID</td>
<td style="TEXT-ALIGN: left;">产品组合代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="2a843b28-3ba3-40cc-b94e-7dbdfe81d8cd"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1023fd74-f5c2-4971-8a08-265aeb836791"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="7a48a7d1-91e8-432e-acb6-4b54a34177d0"></span>
## 5.FAQ
<p>无</p>
