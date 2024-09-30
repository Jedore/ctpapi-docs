<p>请求RCAMS品种内风险对冲参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINTRAPARAMETER/">OnRspQryRCAMSIntraParameter</a></p>
<span class="anchor" id="549ad0a9-fc35-4a01-a079-4300468790c7"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSIntraParameter(CThostFtdcQryRCAMSIntraParameterField *pQryRCAMSIntraParameter, int nRequestID) = 0;</p>
<span class="anchor" id="e458d877-28d1-4e29-bd1f-d3e743cd2945"></span>
## 2.参数
<p>pQryRCAMSIntraParameter：RCAMS品种内风险对冲参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProductID</td>
<td style="TEXT-ALIGN: left;">产品组合代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="0b816ace-7b39-4a21-b8eb-b8c9554c601c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="84dc122d-b547-4c61-9d8f-15add4ac045b"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="208e7fe3-ac91-41cb-b25b-f8adf63c05c3"></span>
## 5.FAQ
<p>无</p>
