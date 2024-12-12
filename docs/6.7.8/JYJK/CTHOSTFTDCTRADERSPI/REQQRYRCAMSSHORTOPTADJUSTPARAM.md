<p>请求RCAMS空头期权风险调整参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSSHORTOPTADJUSTPARAM/">OnRspQryRCAMSShortOptAdjustParam</a></p>
<span class="anchor" id="efcf8c3a-988d-45a5-8b41-7d54701f78d6"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSShortOptAdjustParam(CThostFtdcQryRCAMSShortOptAdjustParamField *pQryRCAMSShortOptAdjustParam, int nRequestID) = 0;</p>
<span class="anchor" id="a139c9b8-ac3d-4586-a06e-deb8ba577f55"></span>
## 2.参数
<p>pQryRCAMSShortOptAdjustParam：RCAMS空头期权风险调整参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProductID</td>
<td style="TEXT-ALIGN: left;">产品组合代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="102f1c3d-eb1d-4d59-afd5-d6f1c54b6611"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="040eb387-fb3c-4225-b04f-36d7aafa4650"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="f1fb7a49-55ec-4a27-9a15-c9386985527d"></span>
## 5.FAQ
<p>无</p>
